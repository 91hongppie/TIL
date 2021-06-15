// importScripts 함수를 사용하면 workers.js 안에서 외부 스크립트 파일을 읽어 들일 수 있다.
importScripts("prime.js");
onmessage = function(e) { // 메세지가 오면 함수를 실행한다.
    console.log("worker: message recieved");
    var message = e.data; // e.data 는 메세지를 보낼 때 담은 데이터
    var n = parseInt(message); // message의 내용을 Int로 바꿔서 
    // import 한 prime(n)의 결과를 담아 main.js에게 메세지로 보낸다. 
    postMessage(prime(n));
};