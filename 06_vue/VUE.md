# Vue

## SPA(Single-Page Application)

- 모바일에 적합함.
- 단점 : 초기 구동속도가 느림
- 전체 렌더링이 아님(특정부분만)

M(model) <-> ViewModel(V와 M을 결합시킨다.(binding)) <-> View(DOM)

## 기본세팅

- CDN



## 인스턴스 옵션

### el

- Vue 인스턴스와 DOM을 연결(마운트, mount)하는 옵션
- View - View Model 을 연결 시킨다.
- HTML 의 id 나 class 와 마운트가 가능하다.

### data

- Vue 인스턴스의 데이터 객체, 인스턴스의 `속성`이라고도 부름
- 데이터 객체는 반드시 기본객체 `{ }`여야 함
- 객체 내부의 아이템들은 value 로써 모든 타입의 객체를 가질 수 있다.(object, string, integer array...)
- 정의된 속성은 인터폴레이션 `({{}})`을 통해서 View 에서 렌더링 가능
- data 에서도 이벤트리스너와 비슷한 이유로 화살표 함수를 작성해서는 안된다.

---

### methods

- Vue 인스턴스에 추가할 메소드들을 정의하는 곳
- (주의) 메소드를 정의하는데에 화살표함수를 사용해선 안된다.

# Vue directive(지시문)

- 디렉티브는 `v-` 접두사가 있는 특수 속성(attr)이며, 디렉티브 속성의 값은 단일 JS 표현식

### v-for

```html
<li v-for="todo in todos">
    {{ todo }}
</li>
```

### v-if

- 특정 조건을 만족할때만 보여지도록(렌더링되도록) 할수있다.
- `v-else` 는 반드시 `v-if` 엘리먼트 바로 뒤에 와야 인식 가능.
- `v-else-if` 도 존재한다.

```html
<li v-for="todo in todos" v-if="!todo.completed">
    {{ todo.content }}
</li>
```

### v-on

- JS 에서 이벤트리스너랑 비슷한 역할을 함
- 이벤트 리스너는 HTML element 를 querySelector 로 가져와 이벤트를 붙여줬다면, Vue 는 HTML element 자체에 이벤트를 붙여준다.
- `v-on`: 뒤에 오는 친구를 `전달인자` 라고 한다.
- `:` 을 붙여 사용하는, 디렉티브 바로 뒤에 붙는 친구들을 지칭한다.

#### 사용법 2가지

1. inline
2. method 정의

### v-bind

- HTML element 의 속성 값을 변경할 때 사용

### v-model

- input tag  의 value - **View**<-------------->v-model<------------>data(**VM**)

### computed

- 미리 계산된 값을 반환.
- 종속 대상을 따라 저장(캐싱)되는 특성이 있다.
- 연산이 많이 필요한 경우 템플릿 안에서 연산 표현식을 사용하는 것보다 computed 를 사용하는 것을 권장
- `{{ newTodo.split('').reverse().join('') }}`

```vue
computed: {
    reversedNewTodo:  function() {
		return this.newTodo.split('').reverse().join('')
	}
}
```

### View-VM-M(localstorage)

---

### Watch

- Vue 인스턴스의 data 변경을 관찰하고 이에 반응
- 데이터 변경에 대한 응답으로 비동기 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 적합
- 특정 데이터가 변경되었을때 정의한 함수를 실행

### v-if / v-show

- v-if : 조건에 맞지 않으면 렌더링 자체를 하지 않음
- v-show : 조건과 관계 없이 일단 렌더링 후에, 조건에 맞지 않으면 CSS display 속성을 토글해서 숨겨버림.

---

### v-bind

`v-bind:` -> `:`

`v-on:` -> `@`

### Computed vs watch

- computed : 계산해야 하는 `목표 데이터를 정의하는 방식`(선언형 프로그래밍)
- watch : 감시할 데이터를 지정하고 그 `데이터가 바뀌면 특정 함수를 실행하라는 방식`(명령형 프로그래밍)  

## 우선순위

- 동일한 노드에서는 for 가 if 보다 높은 우선순위를 가짐
- 즉, v-if 는 루프가 반복될때마다 실행! (일부 항목만 렌더링 할 때 유용)