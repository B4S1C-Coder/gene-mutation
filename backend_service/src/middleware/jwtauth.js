const JWTUtils = require("../util/jwtutils");
const User = require("../model/user");

exports.jwtauth = async (req, res, next) => {
    const token = req.header("Authorization")?.replace("Bearer ", "");

    if (!token) {
        res.status(401).json({ message: "Bearer Token not provided." });
        return;
    }

    try {
        const decoded = JWTUtils.verifyToken(token);
        if (decoded) {

            const user = await User.findById(decoded.id);
            
            if (!user) {
                res.status(400).json({ message: "No user associated with token." });
                return;
            }

            req.user = user;
            next();
        }
    } catch (err) {
        console.log(`[ JWTAuthError ] ${err}`);
        res.status(401).json({ message: "Invalid Token." });
    }
};