const express = require("express");
const router = express.Router();
const imagenetController = require("../controller/imagenet.controller");

const multer = require("multer");

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

router.post("/imagenet-label", upload.single("file"), imagenetController.predictLabel);

module.exports = router;