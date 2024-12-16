const dotenv = require("dotenv");

dotenv.config();

exports.apiKeyMiddleware = async (req, res, next) => {
    try {
        const providedKey = req.header("x-api-key");
        if (!providedKey) {
            res.status(400).json({ message: "API Key not provided." });
            return;
        }

        if (providedKey !== process.env.API_KEY) {
            res.status(401).json({ message: "Invalid API Key." });
            return;
        }

        next();
    } catch (err) {
        console.log(err);
    }
};