const express = require("express");
const router = express.Router();
const userController = require("../controller/user.controller");

const JWTAuth = require("../middleware/jwtauth");

router.post("/login", userController.login);
router.post("/create", userController.createUser);
router.get("/detail", JWTAuth.jwtauth, userController.userDetail);

module.exports = router;