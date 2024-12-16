const PROTO_PATH = __dirname + "/../../../protos/imagenet.proto";

const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const dotenv = require("dotenv");

dotenv.config();

const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    }
);

const imagenet_proto = grpc.loadPackageDefinition(packageDefinition).imagenet;

const client = new imagenet_proto.imagenetService(
    process.env.IMAGENET_SERVICE_TARGET,
    grpc.credentials.createInsecure()
);

exports.predictLabel = (data) => {
    return new Promise((resolve, reject) => {
        client.predictLabel({fileData: data}, (err, response) => {
            if (err != null) {
                console.log(err);
                reject(err);
            } else {
                const predictedLabel = response.predictedLabel;
                console.log(predictedLabel);
                resolve(predictedLabel);
            }
        });
    });
};