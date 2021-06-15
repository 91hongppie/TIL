window.onload = function() {
    var color = document.getElementById("color"),
        dropbox = document.getElementById("dropbox");
    // 드래그를 시작할 때 색상 값을 dataTransfer 객체의 데이터로 설정한다.
    color.ondragstart = function(e) {
        e.dataTransfer.setData("text/plain", e.target.value);
    };
    // 드래그 타깃 요소 위에 마우스 포인터가 올라가면 브라우저 기본 동작을 취소한다(필수)
    dropbox.ondragover = function(e) {
        e.preventDefault();
    };
    // 요소를 드롭하면 dataTransfer의 데이터로 보더 박스 배경색을 설정한다
    dropbox.ondrop = function(e) {
        e.preventDefault();
        e.target.style.backgroundColor = e.dataTransfer.getData("text/plain");
    };
};
