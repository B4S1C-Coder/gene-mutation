from concurrent import futures
import logging

import grpc
import imagenet_pb2
import imagenet_pb2_grpc

from model import resNet50ImagenetLabelPridictor

predictor = resNet50ImagenetLabelPridictor()

class imagenetService(imagenet_pb2_grpc.imagenetServiceServicer):
    def predictLabel(
        self, request: imagenet_pb2.predictLabelRequest, context
    ) -> imagenet_pb2.predictLabelReply:

        data: bytes = request.fileData
        label: str = predictor.predict_label(predictor.prepare_image(data))

        return imagenet_pb2.predictLabelReply(predictedLabel=label)

def runServer():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    imagenet_pb2_grpc.add_imagenetServiceServicer_to_server(imagenetService(), server)
    server.add_insecure_port("[::]:"+port)
    server.start()

    print(f"Server started on port: {port}")
    server.wait_for_termination()

if __name__ == "__main__":
    runServer()
