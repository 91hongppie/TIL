window.onload = function() {
    var N = "10000000",
        mainstart = document.querySelector("#mainstart"),
        workerstart = document.querySelector("#workerstart"),
        clear = document.querySelector("#clear"),
        output = document.querySelector("#output");
        startClock();

    // Worker 객체를 생성한다
    var worker = new Worker("worker.js");
    // message 이벤트 처리기를 등록한다.
    // worker에서 메세지가 도착했을 때, e에는 메세지의 내용이 담겨있다.
    worker.onmessage = function(e) { 
        console.log("recieved: " + new Date());
        output.innerHTML = N + " 이하의 최대 소수 = " + e.data;
    };
    // 워커로 처리한다.
    // 메세지에 N을 담아 worker.js로 보낸다.
    workerstart.onclick = function() {
        console.log("send: " + new Date());
        worker.postMessage(N);
    }
    // 메인 스레드로 처리한다.
    mainstart.onclick = function() {
        /* 
        main.html에서 main.js와 prime.js 모두를 src로 연결했기 때문에
        main.js에서 prime(N)을 사용할수 있다.
        */
        output.innerHTML = N + " 이하의 최대 소수 = " + prime(N);
    }
    // 결과를 지운다.
    clear.onclick = function() {
        output.innerHTML = "";
    };
};

function startClock() {
    var clock = document.querySelector("#clock"),
        startTime = new Date();
    
    setInterval(function() {
        clock.innerHTML = ((new Date() - startTime)/1000).toFixed(1);
    }, 100);
}