// createElement()의 세 번째 매개변수가 문자열이면, 이는 생성하는 엘리먼트의 텍스트 값이다.
let h1 = React.createElement('h1', null, 'Hello World!!!!!')
ReactDOM.render(
    // 세 번째 또는 그 이후의 매개변수가 문자열이 아니라면, 이는 새로 생성하는 엘리먼트의 자식 엘리먼트이다.
    React.createElement('h1', null, h1, h1),
    document.getElementById("content")
)