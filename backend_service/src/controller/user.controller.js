const User = require("../model/user");
const JWTUtils = require("../util/jwtutils");

exports.userDetail = async (req, res) => {
    try {
        res.json(req.user);           
    } catch (err) {
        console.log(err);
        res.status(500).json({ message: "Internal server error." });
    }
};

exports.login = async (req, res) => {
    try {
        const { email, password } = req.body;

        const user = await User.findOne({ email: email });
        if (!user) {
            res.status(404).json({ message: "No user associated with that email." });
            return;
        }

        console.log(user);

        const isPasswordCorrect = await user.comparePassword(password);
        if (!isPasswordCorrect) {
            res.status(401).json({ message: "Invalid password." });
        }

        const token = JWTUtils.createToken(user);
        res.json({ token: token });
    } catch (err) {
        console.log(err);
        res.status(500).json({ message: "Internal server error." });
    }
};

exports.createUser = async (req, res) => {
    try {
        const user = new User(req.body);
        const savedUser = await user.save();

        res.status(201).json({ email: user.email });
    } catch (err) {

        if (err.name === "ValidationError") {
            const errors = Object.values(err.errors).map((error) => error.message);
            res.status(400).json({ message: "Invalid creation parameters", ...errors });
            return;
        }

        console.log(err);
        res.status(500).json({ message: "Internal server error." });
    }
};