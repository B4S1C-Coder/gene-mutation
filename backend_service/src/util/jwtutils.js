const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");

dotenv.config();

exports.createToken = (user) => {
    return jwt.sign(
        { id: user._id }, // PAYLOAD
        process.env.JWT_SECRET,
        { expiresIn: "30d" }
    );
};

exports.verifyToken = (token) => {
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        return decoded;
    } catch (err) {
        console.log(`[ JWTverificationError ] ${err}`);
        return false;
    }
};