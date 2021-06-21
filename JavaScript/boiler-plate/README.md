# ExpressJs

## 시작하기

1. 프로젝트 폴더 만들기 (boiler-plate)

2. `npm init` 

3. index.js 생성

4. `npm i express -S`

5. package.json 파일의 scripts에 `"start": "node index.js"`하면 `npm run start` 로 실행시킬수 있다.

6. mongoose 설치 `npm i mongoose -S` -> MongoDB 사이트에 들어가서 cluster를 만든 후에 DB와 연결

   1. CONNECT 클릭

   2. Connect your application 클릭

   3. Node.js 선택한 뒤에 **Add your connection string into your application code** 밑의 코드를 복사해서 index.js 에 붙여넣기(<password> 에는 본인의 비밀번호를 넣는다.)

   4. ```javascript
       mongoose.connect("mongodb+srv://kyuhong:<password>@boiler-plate.v1suj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", {
          useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
      }).then(() => console.log("MongoDB Connected..."))
        .catch(err => console.log(err));
      ```

7. `npm run start`





## MongoDB Model & Schema

### Model은 schema를 감싸주는 역할을 하고 schema는 하나하나의 정보들을 지정해줄 수 있는것((ex)정보의 타입, 정보의 길이)

1. Model 만들기

   ```javascript
   const mongoose = require("mongoose");
   
   const userSchema = mongoose.Schema({ // Schema
       name: {
           type: String,
           maxlength: 50
       },
       email: {
           type: String,
           trim: true, // abd djg@gmail.com -> abddjg@gmail.com 빈틈을 없애준다.
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
       role: { // 유저의 권환 분류 - 1 = 관리자, 0 = 일반유저...
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
   
   module.exports = { User } // 다른 js 파일에서 쓸 수 있도록 exports를 쓴다.
   ```




## body-parser

- 클라이언트 POST request data의 body로부터 파라미터를 편리하게 추출합니다.

- 설치방법

  - ```bash
    npm install body-parser --save
    ```

  ```javascript
  // index.js
  const bodyParser = require("body-parser");
  // application/x-www-form-urlencoded - 이렇게 된 데이터를 분석해서 가져올수있게 해준다.
  app.use(bodyParser.urlencoded({extended: true}));
  
  // application/json - json으로 된 것을 분석해서 가져올수있게 해준다.
  app.use(bodyParser.json());
  ```

  

## Key.js

- 비밀 정보를 로컬 환경과 배포 환경에서 다르게 가져오기 위해 사용한다.

```javascript
/*
    process.env.NODE_ENV - local에서 하면 development로
    배포 된 상태에서는 production으로 나온다.
*/
if (process.env.NODE_ENV === 'production') {
    module.exports = require('./prod')
} else {
    module.exports = require('./dev')
}
```

- index.js에서 require("key") 하여 사용한다.

## Nodemon

- 변경된 내용을 서버를 닫았다가 다시 열지 않아도 적용된다.

- 개발 환경에서만 사용할 것

- 설치방법

  - ```bash
    npm install nodemon --save-dev
    ```

  - 뒤에 -dev를 붙임으로써 개발환경에서만 적용된다.

- package.json 파일의 scripts에 `"backend": "nodemon index.js",` 를 추가함으로써 `npm run backend` 로 사용할 수 있다.

# Bcrypt로 비밀번호 암호화

- 설치방법

  - ```bash
    npm install bcrypt --save
    ```

- 사용 방법

  - User.js (모델 파일)

    ```javascript
    const bcrypt = require("bcrypt"), // bcrypt를 가져온다
          saltRounds = 10; // salt의 글자수(여기서는 10글자)
    
    
    /*
    	유저 모델에 유저 정보를 저장하기 전에 function(next)를 실행한다. 
    	next는 함수가 끝난 뒤에 next()를 호출하여 index.js의 user.save로 보낸다.
    */
    userSchema.pre('save', function(next) { 
        var user = this;	// this는 userSchema
        /* 
        	email이나 기타 다른 정보를 변경할 때는 실행하지 않는다. 
        	모델의 field 중에 password가 변환될때만 암호화를 진행한다.(가입할 때는 물론 진행)
        */
        if (user.isModified('password')) {
            // 비밀번호를 암호화 시킨다.
          	/* 
              saltRounds = salt의 글자수(여기서는 10자리의 salt를 생성)
              salt를 생성한다.
              salt를 이용해서 비밀번호를 암호화 한다.
    				*/
          	// genSalt = saltRounds와 같은 글자수의 salt를 만든다
            bcrypt.genSalt(saltRounds, function(err, salt) { // function(err, salt) = salt를 생성한다. 
              	// salt를 생성하는데 err이 발생했을 때 next(err)로 index.js의 user.save로 err을 담아 보낸다.
                if (err) return next(err);
              	// salt가 정상적으로 생성됐을 때
              	// salt를 이용하여 비밀번호를 암호화한다. hash가 암호화 된 비밀번호
                bcrypt.hash(user.password, salt, function(err, hash) {
                  	// hash가 정상적으로 생성되지 않았을 때 return next(err); 실행
                    if (err) return next(err); // err이 발생했을 때 index.js의 user.save로 err을 담아 보낸다.
                  	// hash가 정상적으로 생성됐을 때
                    user.password = hash // hash가 정상적으로 생성되면 user.password에 적용한다.
                    next(); // 비밀번호를 암호화하는게 모두 정상적으로 진행되면 err 없이 index.js의 user.save로 돌아간다.
                })
            })
        } else { // 비밀번호 외의 것들을 바꿀 때
          next();
        }
    })
    ```

## 로그인 기능 만들기 - 1

- index.js

  ```javascript
  const cookieParser = require("cookie-parser");
  
  app.use(cookieParser());
  
  
  app.post("/login", (req, res) => { // localhost:3000/login 에서 POST 요청이 왔을 때
    // 요청된 이메일을 데이터베이스에 있는지 찾는다.
    // User 모델에서 req.body.email과 맞는 email이 있는지 찾는다. findOne = mongoDB에서 제공하는 method
    User.findOne({ email: req.body.email }, (err, user) => {
      if (!user) { // 요청으로 들어온 email과 같은 email일 DB에 없을때
        return res.json({
          loginSuccess: false,
          message: "제공된 이메일에 해당하는 유저가 없습니다."
        })
      }
    // 요청된 이메일이 데이터베이스에 있다면 비밀번호가 일치하는지 확인
    // User.js의 userSchema의 method인 comparePassword를 호출한다.
    user.comparePassword(req.body.password, (err, isMatch) => { // user의 메서드인 comparePassword를 실행
      if(!isMatch) {
        return res.json({ loginSuccess: false, message: "비밀번호가 틀렸습니다."})
      }
      // 비밀번호가 일치한다면 Token을 생성하기
      // User.js의 userSchema의 method인 generateToken을 호출한다.
      user.generateToken((err, user) => {
        if(err) return res.status(400).send(err);
  
        // 토큰을 저장한다. where? = 쿠키, 로컬스토리지
        // 쿠키에 저장하기 위해 cookie-parser 라이브러리 설치
        res.cookie("x_auth", user.token) // 쿠키에 키 값을 x_auth로 하여 토큰을 저장한다.
        .status(200) // 200은 요청이 성공했음을 나타낸다
        .json({ loginSuccess: true, userID: user._id }); // json을 담아서 응답
  
      })
    })
    })
  })
  ```

- User.js

  ```javascript
  const jwt = require("jsonwebtoken");
  
  // plainPassword = index.js에서 req.body.password
  // method 이름인 comparePassword는 마음대로 만들어도 되지만 index.js에서 호출할때는 맞춰서 똑같이 써야한다.
  userSchema.methods.comparePassword = function(plainPassword, cb) {
      /* 
      	plainPassword ex)1234567, 
        암호화된 비밀번호 ex)$2b$10$j54n7b80DwuBY/OlpVD3zeb8PjgbAiX1b4s0Lnuk37DespAJQ9YXO 둘을 확인한다.
    	*/
    	// 암호화된 비밀번호와 plainPassword가 일치하는지 비교하여 확인한다.
      bcrypt.compare(plainPassword, this.password, function(err, isMatch) {
          if (err) return cb(err); // 비밀번호가 다르면 콜백함수에 에러를 담아서 리턴한다.
          cb(null, isMatch); // 비밀번호가 같다면 err를 비워두고 isMatch는 true
      })
  }
  
  
  userSchema.methods.generateToken = function(cb) {
  		// this는 index.js에서 호출할 때의 user
      var user = this;
      // jsonwebtoken을 이용해서 토큰을 생성하기
      // user._id에 toHexString()을 붙여줘야한다.
    	// user._id 와 secretToken을 합쳐서 토큰을 생성
      var token = jwt.sign(user._id.toHexString(), 'secretToken'); 
      this.token = token;
      user.save(function(err, user) {
          if (err) return cb(err);
          cb(null, user);
      })
  }
  
  ```

- cookie-parser 설치 방법

  - ```bash
    npm install cookie-parser --save
    ```

  - ```javascript
    const cookieParser = require("cookie-parser");
    
    app.use(cookieParser());
    ```

  - 이 과정을 완료하고나서 app 에서 cookie-parser 사용 가능하다.

- jsonwebtoken 설치 방법

  - ```bash
    npm install jsonwebtoken --save
    ```

  - ```javascript
    const jwt = require("jsonwebtoken")
    ```

  - ```javascript
    // User.js
    var token = jwt.sign(user._id.toHexString(), 'secretToken');
    ```

  - jwt를 사용하여 user._id와 'secretToken' 을 합쳐서 토큰을 만든다.

  - toHexString()을 쓰지않으면 에러가 난다. 

  - toHexString()은 toString()에 포함되는 것으로 더 좁은 의미의 함수이기 때문에 예외발생률이 적어서 사용되는 것 같다.(MongoDB에서 제공하는 예제 코드에서도 toHexString()을 사용한다.)

## Auth 기능 만들기

- cookie에 저장된 Token을 가져와서 복호화를 한다.

1. index.js

```javascript
const { auth } = require("./middleware/auth"), // auth를 가져온다.

// /api/users/auth 를 통해 GET 요청이 들어온다.
// auth를 호출하여 요청이 들어온 정보와 일치하는 유저를 찾는다. 일치하는 유저가 있으면 auth 함수에서 next를 하여 다음 함수로 넘어간다.
// (req, res) =>  화살표 함수로 넘어온다.
// 200과 json 데이터를 응답한다.
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
```

2. middleware/auth.js

```javascript
const { User } = require("../models/User"); // User 모델을 가져온


let auth = (req, res, next) => {

    // 인증 처리를 하는 곳
    // 클라이언트 쿠키에서 토큰을 가져온다.
  	// 들어온 요청에서 쿠키에 있는 토큰을 token에 할당
    let token = req.cookies.x_auth;

    // 토큰을 복호화 한 후 유저를 찾는다.
  	// 유저가 있으면 인증 Okay
    // 유저가 없으면 인증 No
    User.findByToken(token, (err, user) => {
        if (err) throw err;
        if (!user) return res.json({ isAuth: false, error: true });

        req.token = token;
        req.user = user;
        next(); // index.js 에서 auth 다음으로 넘어가기 위해 next()를 호출한다.
    })
} 

module.exports = { auth };
```

3. User.js

```javascript
userSchema.statics.findByToken = function(token, cb) {
    var user = this;
    
    // 토큰을 decode 한다.
  	// 유저를 찾으려고 decode하는데 token으로 찾을 수 있기 때문에 굳이 필요없는듯하다.
    jwt.verify(token, 'secretToken', function(err, decoded) {
        // 유저 아이디를 이용해서 유저를 찾은 다음에
        // 클라이언트에서 가져온 token과 DB에 보관된 token이 일치하는지 확인
				// 일치하는 정보가 있는지 찾는다 "_id": decoded는 없어도 된다.
      	// "token": token만 있어도 token은 유일하기 때문에 찾을수 있다.
      	// findOne은 MongoDB에서 지원하는 함수
        user.findOne({ "_id": decoded, "token": token }, function(err, user) {
            if (err) return cb(err);
            cb(null, user);
        })
    })
}
```

## 로그아웃

1. 로그아웃 Route 만들기
2. 로그아웃하려는 유저를 데이터 베이스에서 찾는다.
3. 해당 유저의 토큰을 지워준다.

```javascript
// GET 요청을 보낸다.
// auth를 통해 토큰과 일치하는 유저가 있는지 먼저 확인한다. 맞으면 auth에서 next()를 호출하여 다음 함수로 넘어간다.
// findOneAndUpdate는 req의 정보와 일치하는 유저를 찾아 정보를 업데이트한다.
// findOneAndUpdate(a, b, c) = a와 일치하는 유저를 찾아 b의 정보로 업데이트 한 다음에 c 함수를 실행한다.
app.get("/api/users/logout", auth, (req, res) => {
  User.findOneAndUpdate({ _id: req.user._id }, // DB에서 user의 정보와 맞는 데이터를 찾는다.
    { toke: "" },	// 찾은 데이터의 token 값을 비워준다.
    (err, user) => {
      if (err) return res.json({ sccess: false, err}); // 에러가 발생했을 때
      return res.status(200).send({ // 모든게 무사히 끝났을 때 { success: true} 를 담아서 200 응답한다.
        success: true
      })
    })
})
```





# React JS

## React란?

- 2013년 페이스북에서 출시한 라이브러리
- module과 비슷하게 컴포넌트로 이뤄져 있어서 재사용성이 뛰어남
- Virtual DOM
  - 만약 10개의 리스트가 있다.
  - 그 중에 한가지의 리스트만 Update 됐다.
  - 그 바뀐 한 가지 아이템만 DOM에서 바꿔준다.
  - 어떻게? (Real DOM에서는 전체  리스트를 다시 Reload 해야된다.)
    - Virtual DOM은 Real DOM을 가볍게 copy한 것
    - Virtual DOM이 이전 Virtual DOM에서 찍어둔 Snapshot과 비교를 해서 바뀐 부분을 찾는다.(이 과정을 diffing이라고 부름)
    - Real DOM에서 바뀐 부분만 바꿔준다.

## Create-React-App

- 원래 리액트 앱을 처음 실행하기 위해선 webpack 이나 babel 같은 것을 설정하기 위해서 엄청나게 많은 시간이 걸렸다.
  - babel - 최신 자바스크립트 문법을 지원하지 않는 브라우저들을 위해서 최신 자바스크립트 문법을 구형 브라우저에서도 돌아갈수있게 변환 시켜줌
  - webpack - 복잡한 파일 구조를 webpack을 이용해서 번들화(묶어주는) 시켜준다. 많은 모듈들을 합쳐서 간단하게 만들어준다.

### 시작하기

- 파일구조를 새롭게 한다.

  - client 폴더와 server 폴더를 만든다.
    - server (Back-end)
      - config
      - middleware
      - models
      - index.js
    - client (Front-end)

- client 폴더로 이동한다.

  - ```bash
    cd client
    ```

- create-react-app

  - ```bash
    npx create-react-app .
    ```

## NPM VS NPX

### What is NPM? (Node Package Manager)

- 레지스트리(저장소) 역할

- 어플리케이션 실행할 때

- 배포할 때 build

  - ```bash
    npm run build
    ```

- npm install locally

  - ```bash
    npm install
    ```

  - 프로젝트 내의 node_modules에 다운 받아진다.

- npm install globally

  - ```bash
    npm install -G
    ```

  - 컴퓨터 전체에서 사용할 수 있도록 다운 받아진다.

- 만약 Install하는 npm을 다른 프로젝트에서 쓰지 않는다면 Global로 Install 할 필요가 없다. Disk Space를 낭비하지 않기 위해

## NPX

1. 원래 create-react-app 할 때 `npm install -g create-react-app` 이렇게 해서 Global 디렉토리에 다운받음
2. 이제는 npx를 이용하여 그냥  create-react-app을 이용 할 수 있음
3. npx가 npm registry에서 create-react-app을 찾아서(look up) 다운로드 없이 실행 시켜준다.

### NPX의 장점

1. Disk Space를 낭비하지 않을 수 있다.
2. 항상 최신 버전을 사용할 수 있다.
