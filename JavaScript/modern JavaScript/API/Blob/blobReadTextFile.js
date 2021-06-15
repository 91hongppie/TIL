function readTextFile(f, callback) {
    var reader = new FileReader();  // FileReader 객체를 생성한다.
    reader.onload = function() {    // onload 이벤트 처리기를 정의한다.
        callback (reader.result);   // 읽어 들인 텍스트를 callback에 전달한다.
    };
    reader.onerror = function(e) {  // 오류가 발생하면
        console.log("Error", e);    // 로그로 남긴다.
    };
    reader.readAsText(f);           // 파일의 데이터를 읽어 들인다.
}
window.onload = function() {
    var input = document.getElementById("input");
    var output = document.getElementById("output");
    input.onchange = function(e) {
        var files = e.target.files;
        // 텍스트 파일인지 확인한다.
        if ( files[0].type.substring(0, 5) !== "text/" ) return;
        // File 객체의 데이터를 읽어서 pre 요소에 기록한다.
        readTextFile(files[0], function(text) {
            output.innerHTML = text;
        });
    };
};