# CH03

## JSX 

### JSX로 React 엘리먼트 생성하기

```javascript
// 자바스크립트로 작성한 Hello World
ReactDOM.render(
	React.createElement('h1', null, 'Hello world!'),
  document.getElementById('content')
)
// JSX로 작성한 Hello World
ReactDOM.render(
	<h1>Hello world!</h1>,
  document.getElementById('content')
)
// JSX 문법으로 작성한 객체도 변수에 저장할 수 있다.
let helloWorldReactElement = <h1>Hello world!</h1>
ReactDOM.render(
	helloWorldReactElement,
  document.getElementById('content')
)

```

### React 컴포넌트에 JSX 사용하기

```javascript
// JSX를 이용해서 생성한 HelloWordl 클래스
// ReactDOM.render에서 호출할 때 <클래스이름/>를 사용한다. 반드시 대문자로 시작
// class에서 return 문의 같은 행에 이후로 아무것도 적지 않는 경우에는 반드시 괄호를 넣어야한다.
/*
	return 문과 같은 줄에서 시작하여 괄호를 생략할 수도 있다.
	단점음 여는 <div> 태그가 눈에 잘 띄지 않는다는 점.
	render() {
		return <div>
		</div>
	}
*/
class HelloWorld extends React.Component {
  render() {
    return (
    <div>
    	<h1>1. Hello World!</h1>
    	<h1>2. Hello World!</h1>
    </div>
    )
  }
}
ReactDOM.render(
	<HelloWorld/>,
	document.getElementById('content')
)
```

### JSX에서 변수 출력하기

```jsxjavascript
// 일반 자바스크립트에서 현재 날짜/시간 표시하기
class DateTimeNow extends React.Component {
  render() {
    let dateTimeNow = new Date().toLocaleString()
    return React.createElement(
    	'span',
    	null,
    	`Current date and time is ${dateTimeNow}.`
    )
  }
}
// JSX에서 현재 날짜/시간 표시하기
// 지역변수뿐만 아니라 속성도 출력할 수 있다.
// 어떤 자바스크립트 코드라도 중괄호 안에서 실행 시킬 수 있다.
// <p>Current date and time is {new Date().toLocaleString()}.</p> 이런 식으로 사용 가능
class DateTimeNow extends React.Component {
  render() {
    let dateTimeNow = new Date().toLocaleString()
    return <span>Current date and time is {dateTimeNow}.</span>
  }
}
```

```javascript
// JSX에서 변수 출력하기
let helloWorldReactElement = <h1>Hello World!</h1>
class HelloWorld extends React.Component {
  render() {
    return (
    	<div>
    		{helloWorldReactElement}
    		{helloWorldReactElement}
  		</div>
		)
  }
}
ReactDOM.render(
	<HelloWorld/>,
	document.getElementById('content')
)
```

### JSX에서 속성 사용하기

```javascript
// JSX를 이용한 하드코딩
ReactDOM.render((
	<div>
		<a href="http://reactquickly.co">Time for React?</a>	// 표준 HTML 속성인 href를 렌더링한다.
		<DateTimeNow userName='Azat'/>	// userName 속성의 값을 설정한다.
	</div>
	),
  document.getElementById('content')
)
// JSX를 이용한 동적코딩
// 속성 값은 ProfileLink 생성 시에 정의된다.
// 즉, ProfileLink를 생성하는 부모 컴포넌트에서 이 값을 정의하는 것이다.
class ProfileLink extends React.Component {
  render() {
    return (
    <a href={this.props.url}
  			title={this.props.label}
				target="_blank">Profile
		</a>
    )
  }
}
```

```javascript
// 사용자 지정 데이터를 속성으로 추가하는 경우
<li react-is-awesome="true" id="320">React is awesome!</li>
/*
	DOM의 HTML 비표준 속성에 데이터를 저장하는 것은 일반적으로 안티패턴으로 여겨진다.
	DOM을 데이터베이스나 프론트엔드 데이터 저장소로 사용하는 것이 적절하지 않기 때문이다.
	DOM에서 데이터를 가져오는 것은 메모리 상의 가상 저장소에서 데이터를 가져오는 것보다 느리다.
	JSX를 사용할 때 데이터를 반드시 HTML요소의 속성으로 저장해야 하는 경우에는 data-* 속성을 사용한다.
	예를 들어 속성에서 <li>요소에 this.reactIsAwesome 값을 렌더링하려면 다음과 같이 작성할 수 있다.
*/
<li data-react-is-awesome={this.reactIsAwesome}>React is awesome!</li>
// this.reactIsAwesome의 값이 true라면 HTML 렌더링 결과는 다음과 같다.
<li data-react-is-awesome="true">React is awesome!</li>

// data-* 를 사용하지않으면 원하는 결과가 나오지않는다.
<li react-is-awesome={this.reactIsAwesome}>React is orange</li>
<li reactIsAwesome={this.reactIsAwesome}>React is orange</li>
// 결과는 다음과 같다
// <li>React is orange</li>
```

```javascript
// 자바 스크립트 코드
class HelloWorld extends React.Component {
  render() {
    return React.createElement(
    	'h1',
    	this.props,
    	'Hello ' + this.props.frameworkName + ' world!!!'
    )
  }
}
// JSX 코드
// 이 방법은 안티패턴으로 추천하지 않는다.
class HelloWorld extends React.Component {
  render() {
    return <h1 title={this.props.title} id={this.props.id}>
      Hello {this.props.frameworkName} world!!!
    </h1>
  }
}
// {...this.props}를 사용하면 모든 속성을 자식 엘리먼트로 전달할 수 있다.
class HelloWorld extends React.Component {
  render() {
    return <h1 {...this.props}>Hello {this.props.frameworkName} world!!</h1>
  }
}

ReactDOM.render(
	<div>
  	<HelloWorld
  		id='ember'
  		frameworkName='Ember.js'
  		title='A framework for creating ambitious web applications.' />
    <HelloWorld
        id='backbone'
        frameworkName='Backbone.js'
        title='Backbone.js gives structure to web application...' />
    <HelloWorld
        id='angular'
        frameworkName='Angular.js'
        title='Superheroic JavaScript MVW Framework' />
  </div>,
  document.getElementById('content')
)
```

