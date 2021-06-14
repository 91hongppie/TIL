const mongoose = require("mongoose");

const userSchema = mongoose.Schema({
    name: {
        type: String,
        maxlength: 50
    },
    email: {
        type: String,
        trim: true,
        unique: 1
    },
    password: {
        type: String,
        minlength: 5
    },
    lastname: {
        type: String,
        maxlength: 50
    },
    role: { // 유저의 권환 분류 - 관리자, 일반유저...
        type: Number,
        default: 0
    },
    image: String,
    token: {
        type: String
    },
    tokenExp: { // 토큰을 사용할 수 있는 기간
        type: Number
    }
})

const User = mongoose.model("User", userSchema); // mongoose.model(모델 이름, 스키마)

module.exports = { User }