# ReactJS

## CH01

### Hello World!

#### React와 ReactDOM을 CDN으로 불러와서 진행

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>hello world</title>
  <!-- React 라이브러리를 불러온다. -->
  <script crossorigin src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
  <!-- ReactDOM 라이브러리를 불러온다. -->
  <script crossorigin src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>  
</head>
<body>
  <div id="content"></div>  <!-- Hello World 뷰를 위한 React 코드를 작성한다. -->
  <script type="text/javascript"> // <div> 요소를 정의하여 React UI를 추가한다.
    // h1 요소를 React 엘리먼트로 생성하여 변수에 담는다.
    // 변수명은 아무거나 써도 되지만 ReactDom.render() 에서 같은 변수명을 제대로 입력해야한다.
    var h1= React.createElement('h1', null, 'Hello World~!!!!!!!');
    // h1 요소를 ID가 content인 실제 DOM에 렌더링한다.
    ReactDOM.render(
      h1,
      document.getElementById('content')
    )
    /*
    ReactDOM.render(
    	React.createElement('h1', null, 'Hello World~!!!!!!!'),
      document.getElementById('content')
    )
    이런 식으로 변수명에 할당하지않고 바로 쓸수도 있다.
    */
  </script>
</body>
</html>
```

#### React 엘리먼트를 직접 \<body>에  렌더링하지 않는 이유는 무엇일까?

- 다른 라이브러리나 \<body>를 조작하는 브라우저 확장 프로그램과 충돌하는 것을 방지하기 위해서다.

- \<body>에 직접 추가하려고 하면 다음과 같은 경고를 확인할 수 있다.

  - ```bash
    Rendering components directly into document.body is discouraged...
    document.body에 직접 컴포넌트를 렌더링하는 것은 권장되지 않습니다...
    ```

#### React 엘리먼트 생성

- ```javascript
  React.createElement(elementName, data, child)
  ```

  - elementName: HTML 태그명을 'h1' 처럼 문자열로 작성하거나 직접 만든 컴포넌트 클래스 객체를 넘겨줄 수 있다.
  - data: 속성이나 상위 컴포넌트에 받는 값으로, null이나 {name: 'Azat'}와 같은 형태의 데이터다.
  - child: 자식 엘리먼트나 태그 내부에 작성하는 텍스트다.



## CH02

### 엘리먼트 중첩

```javascript
// createElement()의 세 번째 매개변수가 문자열이면, 이는 생성하는 엘리먼트의 텍스트 값이다.
let h1 = React.createElement('h1', null, 'Hello World!!!!!')
ReactDOM.render(
    // 세 번째 또는 그 이후의 매개변수가 문자열이 아니라면, 이는 새로 생성하는 엘리먼트의 자식 엘리먼트이다.
    React.createElement('h1', null, h1, h1),
    document.getElementById("content")
)
```

- ReactDOM.render() 에는 하나의 React 엘리먼트만 인자로 전달할 수 있다.
- 지금까지는 createElement()의 첫 번째 매개변수로 문자열만 입력했다. 사실 첫 번째 매개변수로 두 가지 자료형을 입력할 수 있다.
  - 문자열로 작성한 일반적인 HTML 태그
    - 'h1', 'div', 'p' 처럼 화살괄호가 없는 문자열이다.
    - 이름은 소문자로 작성한다.
  - React 컴포넌트 클래스 객체
    - HelloWorld를 예로 들 수 있다.
    - React 컴포넌트 클래스의 이름은 대문자로 시작한다.

### React 컴포넌트 클래스 생성

```javascript
let h1 = React.createElement('h1', null, 'Hello World!!!');
// React 컴포넌트 클래스 정의(이름은 대문자로 시작한다.
// class CHILD extends PARENT
class HelloWorld extends React.Component {
    // 엘리먼트 하나를 반환하는 함수인 render() 메서드를 생성한다.
    render() {
        /*
            return 문에는 React 엘리먼트를 반환하도록 구현하여
            React 클래스가 render()를 실핼하면 두 개의
            <h1> 엘리먼트를 감싼 <div> 엘리먼트를 받을 수 있다.
        */
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
```

- createElement()의 첫 번째 매개변수로 문자열 외에도 사용자 정의 컴포넌트 클래스도 사용할 수 있다.
- ReactDOM.render()와 유사하게, 컴포넌트 클래스의 render() 메서드는 **엘리먼트 하나만 반환한다.**
- 여러 개의 동일 계층 엘리먼트를 반환하려면, \<div>나 \<span> 요소처럼 스타일에 영향을 주지 않는 엘리먼트로 감싸야한다.

### React 속성 사용하기

```javascript
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
```

- React 컴포넌트의 속성(properties)은 React 선언형 스타일의 기초라고 할 수 있다.
- 속성은 **컴포넌트 내부에서는 변경할 수 없는 값**
- 속성은 다음과 같은 용도로 쓸 수 있다.
  - 일반적인 HTML 요소의 속성: href, title, style, class 등
  - React 컴포넌트 클래스의 자바스크립트 코드에서 this.props의 값. 예를 들어 this.props.PROPERTY_NAME(PROPERTY_NAME을 임의의 값으로 정할 수 있음)
- 속성의 기능을 활용해서 속성 값에 따라 렌더링하는 엘리먼트를 아예 다른 모습으로 바꿀수도 있다.
  - 같은 컴포넌트에 다른 속성 값을 입력하면 컴포넌트가 렌더링한 엘리먼트의 모습을 다르게 할 수 있다는 것이다.
  - 속성은 render() 메서드를 통해 렌더링할 수 있고, 컴포넌트 클래스의 코드에서 사용할 수 있으며, HTML 속성으로도 사용할 수 있다.

#### 요약

- React 엘리먼트를 중첩하여 자식 엘리먼트로 추가하려면 createElement()의 세 번째 인자로 계속해서 전달하면 된다.
- React 엘리먼트를 생성할 때 사용자 정의 컴포넌트 클래스를 사용한다.
- 속성을 사용하여 React 엘리먼트의 렌더링 결과를 바꾼다.
- 부모 컴포넌트는 자식 엘리먼트에 속성을 전달할 수도 있다.
- React 컴포넌트를 통해 컴포넌트 기반 아키텍처를 구현할 수 있다.