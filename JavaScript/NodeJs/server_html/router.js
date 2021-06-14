const httpStatus = require("http-status-codes"),
    htmlContentType = {
        "Content-Type": "text/html"
    },
    routes = {  // POST 및 GET 요청에 매핑된 라우트를 저장할 routes 객체의 정의
        "GET": {
            "/info": (req, res) => {
                res.writeHead(httpStatus.OK, {
                    "Content-Type": "text/plain"
                });
                res.end("Welcome to the Info Page!");
            }
        },
        "POST": {}
    };
    // exports는 함수를 내보낼 때 사용, 다른 main.js에서 handle을 사용할 수 있도록 만든다.
    // 모듈이 함수와 객체를 공유할 수 있도록 하기 위한 것이다.
    // 객체가 모듈의 exports 객체에 추가되지 않으면 CommonJS에 정의된 대로 해달 모듈에 로컬로 유지된다.
    exports.handle = (req, res) => { // 라우트에 따른 콜백 함수를 처리하기 위한 함수 handle의 생성
        try {
            if (routes[req.method][req.url]) {
                routes[req.method][req.url](req, res);
            } else {
                res.writeHead(httpStatus.NOT_FOUND, htmlContentType);
                res.end("<h1>No such file exists</h1>");
            }
        } catch(ex) {
            console.log("error: " + ex);
        }
    };

    exports.get = (url, action) => { // main.js로부터 routes에 등록하기 위한 get 및 post 함수 생성
        routes["GET"][url] = action;
    };

    exports.post = (url, action) => {
        routes["POST"][url] = action;
    };