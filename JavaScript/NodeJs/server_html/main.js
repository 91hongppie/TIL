// const port = 3000,
//     http = require("http"),
//     httpStatus = require("http-status-codes"),
//     fs = require("fs"); // fs 모듈의 요청

// --------------------------------------------------------------------------------------

// const routeMap = { // HTML 파일에 매핑되는 라우트 설정
//     "/": "views/index.html"
// };
// http.createServer((req, res) => {
    //     res.writeHead(httpStatus.OK, {
        //         "Content-Type": "text/html"
        //     });
        //     if (routeMap[req.url]) {
            //         fs.readFile(routeMap[req.url], (error, data) => { // 매핑된 파일들의 콘텐츠 읽기
            //             res.write(data); // 파일 콘텐츠로 응답
            //             res.end();
            //         });
            //     } else {
                //         res.end("<h1>Sorry, not found</h1>");
                //     }
                // })
                // .listen(port);
                // console.log(`The server has started and is listening on port number: ${port}`);
                
// --------------------------------------------------------------------------------------

// const getViewUrl = (url) => { // URL을 파일 경로에 보간하기 위한 함수 생성
//     return `views${url}.html`;
// };

// http.createServer((req, res) => {
    //     let viewUrl = getViewUrl(req.url); // 파일 경로 문자열 추출
    //     fs.readFile(viewUrl, (error, data) => { // 요청 URL을 fs file 탐색에 보간
    //         if (error) { // 404 에러 코드 처리
    //             res.writeHead(httpStatus.NOT_FOUND);
    //             res.write("<h1>FILE NOT FOUND</h1>");
    //         } else { // 파일 내용으로 응답
    //             res.writeHead(httpStatus.OK, {
        //                 "Content-Type": "text/html"
        //             });
        //             res.write(data);
        //         }
        //         res.end();
        //     });
        // })
        // .listen(port);
        // console.log(`The server has started and is listening on port number: ${port}`);

// --------------------------------------------------------------------------------------
        
//         const sendErrorResponse = res => { // 에러 핸들링 함수 생성
//             res.writeHead(httpStatus.NOT_FOUND, {
//                 "Content-Type": "text/html"
//             });
//             res.write("<h1>File Not Found</h1>");
//     res.end();
// };

// http.createServer((req, res) => {
//     let url = req.url; // url 변수에 요청 URL 저장
//     if (url.indexOf(".html") !== -1) { // URL에 파일 확장자가 있는지 확인
//         res.writeHead(httpStatus.OK, {
//             "Content-Type": "text/html" // 요청 콘텐츠 유형의 지정
//         });
//         customReadFile(`./views${url}`, res); // 파일을 읽어들이기 위한 readFile의 호출
//     } else if (url.indexOf(".js") !== -1) {
//         res.writeHead(httpStatus.OK, {
//             "Content-Type": "text/javascript"
//         });
//         customReadFile(`./public/js${url}`, res);
//     } else if (url.indexOf(".css") !== -1) {
//         res.writeHead(httpStatus.OK, {
//             "Content-Type": "text/css"
//         });
//         customReadFile(`./public/css${url}`, res);
//     } else if (url.indexOf(".png") !== -1) {
//         res.writeHead(httpStatus.OK, {
//             "Content-Type": "image/png"
//         });
//         customReadFile(`public/images${url}`, res)
//     } else {
//         sendErrorResponse(res);
//     }
// })
// .listen(port)
// console.log(`The server has started and is listening on port number: ${port}`)

// const customReadFile = (file_path, res) => { // 이름으로 요청된 파일 찾기
//     if (fs.existsSync(file_path)) { // 파일이 존재하는지 확인
//         fs.readFile(file_path, (error, data) => {
//             if (error) {
//                 console.log(error);
//                 sendErrorResponse(res);
//                 return;
//             }
//             res.write(data);
//             res.end();
//         });
//     } else {
//         sendErrorResponse(res);
//     }
// };

const port = 3000,
    http = require("http"),
    httpStatusCodes = require("http-status-codes"),
    router = require("./router"),
    fs = require("fs"), // 파일에 액세스하기 위해 필요하다
    plainTextContentType = {
        "Content-Type": "text/plain"
    },
    htmlContentType = {
        "Content-Type": "text/html"
    },
    customReadFile = (file, res) => { // 코드 반복을 줄이기 위한 변경된 readFile 함수의 생성
        fs.readFile(`./${file}`, (errors, data) => {
            if (errors) {
                console.log("Error reading the file...");
            }
            res.end(data);
        });
    };

router.get("/", (req, res) => { // get과 post로 라우트 등록
    res.writeHead(httpStatusCodes.OK, plainTextContentType);
    res.end("INDEX");
});

router.get("/index.html", (req, res) => {
    res.writeHead(httpStatusCodes.OK, htmlContentType);
    customReadFile("/views/index.html", res);
});

router.post("/", (req, res) => {
    res.writeHead(httpStatusCodes.OK, plainTextContentType);
    res.end("POSTED");
});

http.createServer(router.handle).listen(port); // router.js 를 통한 모든 요청 처리
console.log(`The server has started and is listening on port number: ${port}`);
