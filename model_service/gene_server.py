from concurrent import futures
import logging

import grpc
import gene_pb2
import gene_pb2_grpc

from gene_model import GeneModel

predictor = GeneModel()

class geneService(gene_pb2_grpc.MutationPredictionServiceServicer):
    def PredictMutation(
        self, request: gene_pb2.PredictMutationRequest, context
    ) -> gene_pb2.PredictMutationReply:

        data: bytes = request.fnaFileData
        preds = predictor.predict_label(predictor.prepare_image(data))

        return gene_pb2.PredictMutationReply(predictions=preds)

def runServer():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gene_pb2_grpc.add_MutationPredictionServiceServicer_to_server(geneService(), server)
    server.add_insecure_port("[::]:"+port)
    server.start()

    print(f"Server started on port: {port}")
    server.wait_for_termination()

if __name__ == "__main__":
    runServer()
