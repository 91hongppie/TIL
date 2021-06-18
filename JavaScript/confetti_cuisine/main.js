const express = require("express"), // express를 요청
    app = express(),    // express 애플리케이션의 인스턴스화
    layouts = require("express-ejs-layouts"),   // express-ejs-layouts의 요청
    homeController = require("./controllers/homeController"),
    errorController = require("./controllers/errorController");


app.set("view engine", "ejs");  // ejs를 사용하기 위한 애플리케이션 세탕
app.set("port", process.env.PORT || 3000);

app.use(express.static("public"));
app.use(layouts);    // layout 모듈 사용을 위한 애플리케이션 세팅
app.use(express.urlencoded({ extended: false }));   // URL 인코드와 JSON 파라미터 처리를 위한 body-parser의 사용을 Express.js에 선언
app.use(express.json());
app.use(errorController.pageNotFoundError);
app.use(errorController.internalServerError);

app.get("/", (req, res) => {    // 홈페이지를 위한 라우트 생성
    res.send("Welcome to Confetti Cuisine!");
})
app.get("/courses", homeController.showCourses);    // 코스 페이지, 연락처 페이지, 연락처 제출 양식을 위한 라우트의 추가
app.get("/contact", homeController.showSignUp);
app.post("/contact", homeController.postedSignUpForm);

app.listen(app.get("port"), () => { // 3000번 포트로 리스닝 설정
    console.log(`Server running at http://localhost:${app.get("port")}`);
});