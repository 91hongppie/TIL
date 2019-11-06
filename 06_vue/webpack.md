## webpack

- 웹팩은 현재 가장 널리 쓰이는 **모듈 번들러.**
- JS 뿐만 아니라, CSS, IMAGE 파일 등 리소스의 의존성들도 관리한다.

## 모듈

- 어플리케이션을 구성하는 개별적 요소
- 재사용 가능한 코드 조각
- 모듈은 세부사항을 캡슐화한다.
- 특정 기능을 갖는 작은 코드 단위

```javascript
// module.js
function sum(a, b) {
    return a+b
}
function sub(a, b) {
    return a-b
}
function mul(a, b) {
    return a*b
}
export {sum, sub, mul}

// test.js
import * as lib from './module'
import {sum, mul} from './module'

console.log(lib.sub)
```



## 모듈 번들러

- 웹 어플리케이션을 구성하는 자원(HTML, CSS, JS, IMG 등)을 모두 각각의 모듈로 보고 이를 조합해서 병합된 하나의 결과물로 만드는 도구

---

개발을 편하게 모듈 단위 개발 => 모듈끼리 연결(의존성)을 신경쓰기가 어려워짐 => 웹팩아 하나로 만들어줘.

## entry -> `main.js`

- 여러 js 파일들의 시작점 -> 웹팩이 파일을 읽어들이기 시작하는 부분

## module 

- 웹팩은 JS만 변환 가능하기 때문에 html, css 등은 모듈을 통해서 웹팩이 이해할 수 있도록 변환이 필요하다.
- 변환 내용을 담는 곳.

## plugins

- 웹팩을 통해서 번들된 결과물을 추가 처리하는 부분

## output

- 여러 js 파일을 **하나로 만들어 낸 결과물**

---

웹팩은 js 코드만 이해 가능하기 때문에 vue파일(`vue-loader` 설치) 및 html, css 파일(`vue-template-compiler` 설치) 등을 변환하기 위하여 모듈을 설치

---

최상위 컴포넌트(App.vue)

하위 컴포넌트(TodoList.vue)

---

### 컴포넌트 등록 3 steps(App.vue)

1. `<script>` 에 등록할 컴포넌트 불러오기 (import)
2. `export default` 에 `components` 항목에 등록
3. `<template>`  에서 컴포넌트 사용할 수 있도록 작성

---

웹팩을 직접 작성했을 때 만들었던 `webpack.config.js` 가 보이지 않는다.

`vue.config.js`는 `@vue/cli-service` 에 의해 자동으로 로드되는 선택적 구성 파일로 변경 되었다.

vue-cli 3 버전부터 노출되지 않으며, 설정을 추가하기 위해서는 루트 디렉토리에 직접 파일을 만들고 작성해야한다.