const express = require("express"),
    app = express(),
    port = 3000,
    mongoose = require("mongoose"),
    config = require("./config/key"),
    bodyParser = require("body-parser"),
    { User } = require("./models/User");

// application/x-www-form-urlencoded - 이렇게 된 데이터를 분석해서 가져올수있게 해준다.
app.use(bodyParser.urlencoded({extended: true}));

// application/json - json으로 된 것을 분석해서 가져올수있게 해준다.
app.use(bodyParser.json());

mongoose.connect(config.mongoURI, {
    useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
}).then(() => console.log("MongoDB Connected..."))
  .catch(err => console.log(err));




app.get("/", (req, res) => res.send("Hello World!~~~~~안녕하세요!!! 요즘 너무 더워요!! 땀이 너무 나요"))

app.post("/register", (req, res) => {
  
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

app.listen(port, () => console.log(`Example app listening on port: ${port}`));