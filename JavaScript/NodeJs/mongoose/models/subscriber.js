const mongoose = require("mongoose"),
    subscriberSchema = mongoose.Schema({    // mongoose.Schema로 새로운 스키마 만들기
        name: String,   // 스키마 속성 추가
        email: String,
        zipCode: Number
    })

module.exports = mongoose.model("Subscriber", subscriberSchema)