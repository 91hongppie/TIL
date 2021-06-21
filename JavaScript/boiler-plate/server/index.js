const express = require("express"),
    app = express(),
    port = 3000,
    mongoose = require("mongoose"),
    config = require("./config/key"),
    cookieParser = require("cookie-parser"),
    bodyParser = require("body-parser"),
    { auth } = require("./middleware/auth"),
    { User } = require("./models/User");

// application/x-www-form-urlencoded - 이렇게 된 데이터를 분석해서 가져올수있게 해준다.
app.use(bodyParser.urlencoded({extended: true}));

// application/json - json으로 된 것을 분석해서 가져올수있게 해준다.
app.use(bodyParser.json());
app.use(cookieParser());

mongoose.connect(config.mongoURI, {
    useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
}).then(() => console.log("MongoDB Connected..."))
  .catch(err => console.log(err));




app.get("/", (req, res) => res.send("Hello World!~~~~~안녕하세요!!! 요즘 너무 더워요!! 땀이 너무 나요"))

app.post("/api/users/register", (req, res) => {
  
  // 회원 가입 할 때 필요한 정보들을 client에서 가져오면
  // 그것들을 데이터 베이스에 넣어준다.

  const user = new User(req.body);

  user.save((err, doc) => { // save는 mongoDB의 메서드 정보들을 User model에 저장된다
    if (err) return res.json({ success: false, err}); // error가 발생하면 json형식으로 { seccess: false, err} 을 응답한다.
    return res.status(200).json({ // 성공했을때 200과 { seccess: true } 를 응답한다.
      seccess: true
    })
  }) 
})

app.post("/api/users/login", (req, res) => {
  // 요청된 이메일을 데이터베이스에 있는지 찾는다.
  User.findOne({ email: req.body.email }, (err, user) => {
    if (!user) {
      return res.json({
        loginSuccess: false,
        message: "제공된 이메일에 해당하는 유저가 없습니다."
      })
    }
  // 요청된 이메일이 데이터베이스에 있다면 비밀번호가 일치하는지 확인
  user.comparePassword(req.body.password, (err, isMatch) => {
    if(!isMatch) {
      return res.json({ loginSuccess: false, message: "비밀번호가 틀렸습니다."})
    }
    // 비밀번호가 일치한다면 Token을 생성하기
    user.generateToken((err, user) => {
      if(err) return res.status(400).send(err);

      // 토큰을 저장한다. where? = 쿠키, 로컬스토리지
      res.cookie("x_auth", user.token)
      .status(200)
      .json({ loginSuccess: true, userID: user._id });


    })
  })
  })
})


app.get("/api/users/auth", auth, (req, res) => {

  // 여기까지 미들웨어를 통과해 왔다는 얘기는 Authentication이 True라는 말
  res.status(200).json({
    _id: req.user._id,
    isAdmin: req.user.role === 0 ? false : true, // role 0 -> 일반유저, role !== 0 관리자
    isAuth: true,
    email: req.user.email,
    name: req.user.name,
    lastname: req.user.lastname,
    role: req.user.role,
    image: req.user.image

  })
})


app.get("/api/users/logout", auth, (req, res) => {
  User.findOneAndUpdate({ _id: req.user._id },
    { toke: "" },
    (err, user) => {
      if (err) return res.json({ sccess: false, err});
      return res.status(200).send({
        success: true
      })
    })
})



// 애플리케이션 서버에 port(3000)번 포트를 수신하도록 한다. function을 수행한다.
app.listen(port, () => console.log(`Example app listening on port: ${port}`));