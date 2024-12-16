const imagenet_proto = require("../proto/imagenet_proto");
// const multer = require("multer");

exports.predictLabel = async (req, res) => {
    try {
        if (!req.file) {
            res.status(400).json({ message: "File not provided." });
            return;
        }

        const data = req.file.buffer;

        try {

            const predictedLabel = await imagenet_proto.predictLabel(data);
            res.json({ label: predictedLabel });
            return;

        } catch (err) {

            console.log(err);
            res.status(503).json({ message: "Imagenet service is not available." });
            return;
            
        }

    } catch (err) {
        console.log(err);
        res.status(500).json({ message: "Internal server error." });
    }
};