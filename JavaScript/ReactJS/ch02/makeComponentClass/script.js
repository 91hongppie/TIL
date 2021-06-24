let h1 = React.createElement('h1', null, 'Hello World!!!');
// React 컴포넌트 클래스 정의(이름은 대문자로 시작한다.)
class HelloWorld extends React.Component {
    // 엘리먼트 하나를 반환하는 함수인 render() 메서드를 생성한다.
    render() {
        /*
            return 문에는 React 엘리먼트를 반환하도록 구현하여
            React 클래스가 render()를 실핼하면 두 개의
            <h1> 엘리먼트를 감싼 <div> 엘리먼트를 받을 수 있다.
        */
        console.log(Object.isFrozen(this.props));
        return React.createElement('div', null, h1, h1);
    }
}
// React 엘리먼트를 ID가 content인 실제 DOM에 넣어준다.
ReactDOM.render(
    /* 
        첫 번째 인자로 HelloWorld 클래스를 전달하여 엘리먼트를 생성한다.
        이 때 HelloWorld 클래스는 문자열이 아닌 객체다.
    */
    React.createElement(HelloWorld, null),
    document.getElementById('content')
)