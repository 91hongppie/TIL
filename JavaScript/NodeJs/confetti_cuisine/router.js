const httpStatus = require("http-status-codes"),
    contentTypes = require("./content-types"),
    utils = require("./utils");


const routes = { // 라우트 함수를 위한 routes 객체 생성
    "GET": {},
    "POST": {}
};

exports.handle = (req, res) => {    // 요청을 처리하기 위한 handle 함수를 생성한다.
    try {
        routes[req.method][req.url](req, res);
    } catch (e) {
        res.writeHead(httpStatus.OK, contentTypes.html);
        utils.getFile("view/error.html", res);
    }
};

exports.get = (url, action) => {
    routes["GET"][url] = action;
};

exports.post = (url, action) => {
    routes["POST"][url] = action;
};