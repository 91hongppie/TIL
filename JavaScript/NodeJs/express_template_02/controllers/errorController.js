const expressEjsLayouts = require("express-ejs-layouts");
const httpStatus = require("http-status-codes");

exports.respondNoResouceFound = (req, res) => {
    let errorCode = httpStatus.NOT_FOUND;
    res.status(errorCode);
    res.send(`${errorCode} | The page does not exist!`);
}
exports.respondInternalError = (error, req, res, next) => {
    let errorCode = httpStatus.INTERNAL_SERVER_ERROR;
    console.log(`ERROR occurred: ${error.stack}`)
    res.status(errorCode);
    res.send(`${errorCode} | Sorry, our application is experiencing a problem!`)
}


// exports.logErrors = (error, req, res, next) => { // 에러 처리를 위한 미들웨어 추가
//     console.error(error.stack);   // 에러 스택 로깅
//     next(error);    // 다음 미들웨어 함수로 에러 전달
// };