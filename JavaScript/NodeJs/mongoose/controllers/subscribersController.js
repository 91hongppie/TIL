const Subscriber = require("../models/subscriber");
// 데이터베이스로부터의 데이터를 다음 미들웨어 함수로 전달하기 위한 getAllSubscribers의 exports
exports.getAllSubscribers = (req, res) => {   
    Subscriber.find({}, (error, subscribers) => {   // 구독자 모델에서 검색 쿼리
        if (error) next(error); // 에러를 미들웨어 함수로 전달
        req.data = subscribers; // 요청 객체에 대해 몽고DB로부터 돌아온 데이터의 세팅
        console.log(req.data);
        res.render("subscribers", { subscribers: subscribers });
        // next(); // 다음 미들웨어 함수의 진행
    })
}