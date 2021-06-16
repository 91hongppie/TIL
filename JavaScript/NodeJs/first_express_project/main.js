const port = 3000,
    express = require("express"),   // 애플리케이션에 express 모듈 추가
    app = express();                // 상수 app에 express 애플리케이션 할당

app.get("/", (req, res) => {    
    console.log(req.params);
    console.log(req.body);
    console.log(req.url);
    console.log(req.query);    // 홈페이지에 GET 라우트 세팅
    res.send("Hello, Universe!");   // res.send로 서버에서 클라이언트로의 응답 발행
})
app.get("/items/:vegetable", (req, res) => {
    res.send(req.params.vegetable);
});
app.post("/contact", (req, res) => {
    res.send("Contact information submitted successfully.");
})
.listen(port, () => {
    console.log(`The Express.js server has started and is listening on port number: ${port}`);
});