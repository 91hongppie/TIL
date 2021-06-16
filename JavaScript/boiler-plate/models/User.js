const mongoose = require("mongoose")
    bcrypt = require("bcrypt"),
    saltRounds = 10,
    jwt = require("jsonwebtoken");

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

// 유저 모델에 유저 정보를 함수를 실행한 뒤에 저장한다.
userSchema.pre('save', function(next) {
    var user = this;
    
    if (user.isModified('password')) {
        // 비밀번호를 암호화 시킨다.
        bcrypt.genSalt(saltRounds, function(err, salt) {
            if (err) return next(err);
            bcrypt.hash(user.password, salt, function(err, hash) {
                if (err) return next(err);
                user.password = hash
                next();
            })
        })
    } else {
        next();
    }
})

userSchema.methods.comparePassword = function(plainPassword, cb) {
    // plainPassword ex)1234567, 암호화된 비밀번호 ex)$2b$10$j54n7b80DwuBY/OlpVD3zeb8PjgbAiX1b4s0Lnuk37DespAJQ9YXO 둘을 확인한다.
    bcrypt.compare(plainPassword, this.password, function(err, isMatch) {
        if (err) return cb(err);
        cb(null, isMatch);
    })
}

userSchema.methods.generateToken = function(cb) {

    var user = this;
    // jsonwebtoken을 이용해서 토큰을 생성하기
    // user._id에 toHexString()을 붙여줘야한다.
    var token = jwt.sign(user._id.toHexString(), 'secretToken'); // user._id 와 secretToken을 합쳐서 토큰을 생성
    this.token = token;
    user.save(function(err, user) {
        if (err) return cb(err);
        cb(null, user);
    })
}


const User = mongoose.model("User", userSchema); // mongoose.model(모델 이름, 스키마)

module.exports = { User }