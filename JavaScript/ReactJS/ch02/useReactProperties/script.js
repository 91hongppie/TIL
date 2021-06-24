class HelloWorld extends React.Component {
    render() {
        return React.createElement(
            'h1',
            // 모든 속성을 자식 엘리먼트에 전달한다.
            this.props,
            // 세 문자열 "Hello", "this.props.frameworkName", "World!!!" 를 합친다.
            'Hello ' + this.props.frameworkName + ' World!!!'
        )
    }
}

ReactDOM.render(
    React.createElement(
        'div',
        null,
        React.createElement(HelloWorld, {
            id: 'ember',
            // frameworkName은 <h1>의 HTML 표준 속성이 아니므로 별도의 처리를 하지 않는 경우에는 렌더링하지 않는다.
            frameworkName: 'Ember.js',
            // <h1>의 HTML 표준 속성에 해당하는 id와 title은 그대로 렌더링한다.
            title: 'A framework for creating ambitious web applications.'
        }),
        React.createElement(HelloWorld, {
            id: 'backbone',
            frameworkName: 'Backbone.js',
            title: 'Backbone.js gives structure to web applications...'
        }),
        React.createElement(HelloWorld, {
            id: 'angular',
            frameworkName: 'Angular.js',
            title: 'Superheroic JavaScript MVW Frameworkd'
        })
    ),
    document.getElementById('content')
)