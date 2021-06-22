const port = 3000,
    mongoose = require("mongoose"),   // Mongoose 요청
    express = require("express"),
    app = express(),
    Subscriber = require("./models/subscriber"),
    layouts = require("express-ejs-layouts"),
    subscribersController = require("./controllers/subscribersController");


app.use(layouts);
app.set("view engine", "ejs");
mongoose.connect(
    "mongodb://localhost:27017/recipe_db",  // 데이터베이스 커넥션 설정
    {useNewUrlParser: true}
);

const db = mongoose.connection; // db 변수에 데이터베이스 할당


db.once("open", () => { // 애플리케이션이 데이터베이스에 연결됐을 때 메시지 로깅
    console.log("Successfully connected to MongoDB using Mongoose!")
})

var subscriber1 = new Subscriber({
    name: "Jon Wexler",
    email: "jon@jonwexler.com"
}); // 새로운 Subscriber의 초기화

subscriber1.save((error, savedDocument) => {    // subscriber를 데이터베이스에 저장
    if (error) console.log(error);  // 에러 발생 시 다음 미들웨어 함수로 에러를 전달
    console.log(savedDocument); // 저장된 도큐먼트의 로그
});

Subscriber.create(
    {
        name: "Jon Wexler",
        email: "jon@jonwexler.com"
    },
    function (error, savedDocument) {
        if (error) console.log(error);
        console.log(savedDocument);
    }
);

var myQuery = Subscriber.findOne({
    name: "Jon Wexler"  // name이 Jon Wexler인 데이터
})
.where("email", /wexler/); // email 에 wexler가 들어간 데이터
myQuery.exec((error, data) => {
    if (data) console.log(data.name);
})

app.get("/subscribers", subscribersController.getAllSubscribers);

app.listen(port, () => {
    console.log(`Server running on port: ${port}`)
})