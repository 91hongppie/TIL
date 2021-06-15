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