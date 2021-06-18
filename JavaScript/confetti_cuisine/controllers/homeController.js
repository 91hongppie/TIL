var courses = [
    {
        title: "Event Driven Cakes",
        cost: 50
    },
    {
        title: "Asynchronous Artichoke",
        cost: 25
    },
    {
        title: "Object Oriented Orange Juice",
        cost: 10
    }
];

exports.showCourses = (req, res) => {   // 특정 라우트를 위한 콜백 함수 추가
    console.log(courses)
    res.render("courses", {
        offeredCourses: courses // 코스 배열 데이터를 뷰로 전달
    })
}

exports.showSignUp = (req, res) => {
    res.render("contact");
}

exports.postedSignUpForm = (req, res) => {
    res.render("thanks");
}