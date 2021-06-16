const port = 3000,
    express = require("express"),
    app = express(),
    homeController = require("./controllers/homeController");

app.get("/", (req, res) => {
    res.send("http://localhost:3000/items/ 뒤에 아무거나 쳐보세요. 재밌어요.");
});

app.get("/items/:vegetable", homeController.sendReqParam);

// Express.js에 body-parser를 이용해 URL-encoded 테이터를 파싱하도록 요청
app.use(homeController.logRequestPaths);
app.use(express.json());

app.post("/", (req, res) => {   // 홈페이지를 위한 새로운 라우트 생성
    console.log(req.body);      // 요청 본문의 로깅
    console.log(req.query);
    res.send("POST Successful!");
});

app.post("/signup", homeController.userSignUpProcessor);

app.listen(port, () => {
    console.log(`Server running on port: ${port}`);
});