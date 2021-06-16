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