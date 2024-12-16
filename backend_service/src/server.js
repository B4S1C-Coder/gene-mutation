const express = require("express");
const dotenv = require("dotenv");
const connectToMongoDB = require("./db");

dotenv.config();

const app = express();

// Middlewares
const logging = require("./middleware/logging");
const apiKey = require("./middleware/apikey");
// Routes
const userRoutes = require("./route/user.route");
const imagenetRoutes = require("./route/imagenet.route");

// Middlewares
app.use(express.json());
app.use(logging.requestLogging);
app.use(apiKey.apiKeyMiddleware);
// Routes
app.use("/user", userRoutes);
app.use("/imagenet", imagenetRoutes);

connectToMongoDB();

app.get("/status", (req, res) => {
    res.send("Backend is up and running.");
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});