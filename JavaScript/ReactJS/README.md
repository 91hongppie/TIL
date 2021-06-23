# ReactJS

## Hello World!

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