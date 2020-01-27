#  Java Script #4

## 인수가 원시 값일 때 

```javascript
function add1(x) { return x = x + 1 }
var a = 3;
var b = add1(a);
console.log("a = " + a + "b = " + b); // -> a = 3, b = 4
```

- 함수가 호출될 때 변수 a 의 복사본이 인자 x에 할당된다. 즉 인수에 원시 값을 넘기면 그 값 자체가 인자에 전달된다. 이를 가리켜 **값의 전달** 이라고 부른다.
- 이때 변수 a와 변수 x는 다른 영역의 메모리에 위치한 별개의 변수. 따라서 x의 값을 바꾸더라도 a의 값은 바뀌지 않는다.

## 인수가 객체일 때

```javascript
function add1(p) { p.x = p.x +1; p.y = p.y + 1; return p; }
var a = {x:3, y:4};
var b = add1(a);
console.log(a, b); // -> Object {x=4, y=5} Object {x=4, y=5}
```

- 인수로 객체를 넘겼을 때 전달되는 값은 참조 값 -> **참조 전달**
- 이때 인자 p 와 변수 a 는 똑같은 객체를 참조하고 있다.
- 따라서 p.x, p.y 를 수정하는 것은 a.x, a.y를 수정하는 행위와 같다.

### 인수 여러 개를 우아하게 전달하는 방법

- 함수에 넘겨야 하는 인수 개수가 많아지면 다음과 같은 문제가 발생한다.
  - 인수의 순서를 착각하기 쉽다.
  - 함수가 받는 인수 개수를 바꾸면 함수의 호출 방법이 바뀌므로 프로그램 전체를 수정해야한다.

```javascript
function setBallProperties(x, y, vx, vy, radius) { ... }
...
setBallProperties(0, 0, 10, 15, 5);
    
// 함수의 인수를 객체의 프로퍼티에 담아서 함수에 넘기도록 고쳐보자                                             
                                                  
var parameters = {
  x: 0,
  y: 0,
  vx: 10,
  vy: 15,
  radius: 5
},

function setBallProperties(params) { ... }
...
setBallProperties(parameters)
                                    
// 이때 함수 안에서 프로퍼티를 읽는 코드는 params.vx 처럼 표현하면 되므로 인수 순서가 바뀌는 문제가 발생하지 않습니다. 또한 전달하는 인수를 추가하는 경우에도 프로퍼티만 추가하면 되므로 함수를 호출하는 방법을 바꿀 필요가 없다.  

var parameters = {
  x: 0,
  y: 0,
  vx: 10,
  vy: 15,
  radius: 5,
  color: "blue"
},
setBallProperties(parameters)

// 단, 함수 안에서 객체의 프로퍼티를 수정하면 호출한 코드에 있는 인수 객체의 프로퍼티가 함께 바뀌므로 주의해야 한다.
```

## 변수의 유효 범위

### 1. 전역 유효 범위와 지역 유효 범위

```javascript
var a = "global";
function f() {
  var b = "local";
  console.log(a); // -> "global"
  return b;
}
f();
console.log(b);		// -> ReferenceError: b is not defined


a 의 유효범위 = 전체(전역변수)
b 의 유효범위 = function f() 내부 (지역 변수)
```

### 2.변수의 충돌

```javascript
var a = "global";
function f() {
  var a = "local";
  console.log(a); // -> local
  return a;
}
f();
console.log(a); // -> global
```

-  이 코드에서 두 변수는 이름이 같지만 다른 위치의 메모리에 있는 별개의 변수입니다.
- 지역 변수 a 의 유효 범위 안에서 전역 변수 a 는 숨겨집니다.

### 3.함수 안에서의 변수 선언과 변수 끌어올림

```javascript
function f() {
  console.log(a); // -> undefined
  var a = "local";
  console.log(a); // -> local
  return a;
}
// 위의 코드와 같다.
function f() {
  var a;
  console.log(a);
  a = local;
  console.log(a);
  return a;
}
```

### 4. 함수 안에서의 변수 선언 생략

```javascript
function f() {
  a = "local";
  console.log(a);
  return a;
}
f();
console.log(a)
```

- 변수를 선언하지 않은 상태에서 값을 대입하면 전역 변수로 선언된다.
- 변수 a 는 f 의 지역 변수처럼 보이지만 var로 선언하지 않았으므로 실제로는 전역변수

## 블록 유효 범위 : let 과 const

### 1. let 선언자

```javascript
let x = "outer x";
{
  let x = "inner x";
  let y = "inner y";
  console.log(x); // -> inner x
  console.log(y); // -> inner y
}
console.log(x); // -> outer x
console.log(y); // -> ReferenceError: y is not defined
```

- let 으로 선언한 변수의 유효범위는 블록 안이다.
- 자바스크립트 엔진은 var문과 달리 let 문으로 선언한 변수를 끌어올리지 않는다.
- 또한  let 문으로 똑같은 이름을 가진 변수를 선언하면 문법 오류가 발생한다.

### 2.  const 선언자

- const 문은 블록 유효 범위를 가지면서 한 번만 할당할 수 있는 변수(상수)를 선언합니다.
- const로 선언한 상수는 let문으로 선언한 변수처럼 동작하지만 반드시 초기화해야 한다는 차이점이 있다.

```javascript
const c = 2;
// const 문으로 선언한 변수에 다시 대입을 시도하면 타입 오류가 발생합니다.
c = 5;
// const 문으로 선언한 상수 값은 수정할 수 없지만, 상수 값이 객체이거나 배열일 경우에는 프로퍼티 또는 프로퍼티 값을 수정할 수 있습니다.
const origin = {x:1, y:2};
origin.x = 3;
console.log(origin) // -> Object {x:3, y:2}
```

## 함수 리터럴로 함수 정의하기

```javascript
// 함수 선언
function square(x) { return x * x; }
// 함수 리터럴
var square = function(x) { return x * x; };
// 이 코드에서는 function(x) {...} 부분이 함수 리터럴
```

- **함수 리터럴**은 이름이 없는 함수이므로 **익명 함수** 또는 **무명 함수** 라고 부릅니다.

- 함수 선언문에는 끝에 세미콜론을 붙일 필요가 없지만 함수 리터럴을 사용할 때는 끝에 반드시 세미콜론을 붙여야 합니다.

- 함수 선언문으로 정의한 함수와 함수 리터럴로 정의한 함수의 사용법은 같습니다.

- 이는 함수 리터럴과 함수 선언문이 모두 내부적으로 square변수에 함수 객체의 참조를 저장하기 때문입니다.

- 한 가지 차이점이라면 자바스크립트 엔진이 함수 선언문으로 정의한 함수는 끌어올리지만 함수 리터럴로 정의한 함수는 끌어올리지 않는다는 점입니다. 함수 리터럴로 정의한 익명 함수는 변수에 할당한 후에야 비로소 square라는 이름을 갖게 되고, 그 이름으로 호출할 수 있게 됩니다.

- 익명 함수에도 이름을 붙일 수 있습니다.

  - ```javascript
    var square = function sq(x) { return x * x; };
    ```

- 그러나 코드에서 sq 라는 이름은 함수 안에서만 유효하므로 함수 바깥에서는 sq라는 이름으로 함수를 호출할 수 없습니다.

## 객체의 메서드

- 객체의 프로퍼티 중에서 함수 객체의 참조를 값으로 담고 있는 프로퍼티를 가리켜 **메서드**라고 부릅니다.

```javascript
var circle = {
  center: { x:1.0, y:2.0 },
  radius: 2.5;
  area: function () {
    return Math.PI * this.radius * this.radius;
  }
};

// 함수 객체 안에 적힌 this는 그 함수를 메서드로 가지고 있는 객체를 가리킵니다. 위 코드에서는 circle을 가리킵니다.
// 즉, this.radius == circle.radius
// 메서드는 일반 함수와 마찬가지로 소괄호를 붙여서 실행합니다.
circle.area() // -> 19.63495...  
```

## 메서드를 가진 객체를 생성하는 생성자

- 생서자에서 **this.프로퍼티 이름**에 함수의 참조를 대입하면 메서드를 정의할 수 있습니다.
- 이때 메서드 함수 안에 있는 **this**는 생성될 인스턴스를 가리킵니다.

```javascript
function Circle(center, radius) {
  this.center = center;
  this.radius = radius;
  this.ares = function() {
    return Math.PI * this.radius * this.radius;
  };
}
var p = {x:0, y:0};
var c = new Circle(p, 2.0);
console.log("넓이 = " + c.area()); // ->  넓이  = 12.56637..
```

## Function 생성자

```javascript
var square = new Function("x", "return x * x");
// 첫번째 인자인 "x" 는 인수의 이름을 뜻하는 문자열 두번째 인수는 함수 몸통이 작성된 문자열
var 변수 이름 = new Function(첫 번째 인수, ..., n번째 인수, 함수 몸통);
```

- Function생성자로 생성한 함수는 전역 변수와 자신의 지역 변수만 읽고 쓸 수 있다는 단점이 있어서 함수를 동적으로 생성해야 하는 특별한 상황 외에는 사용하지 않습니다.
- 또한 악의를 품은 사용자가 입력한 문자열을 Function 생성자의 인수인 '함수의 몸통'으로 전달하면 악성 코드가 실행되어 보안 문제가 발생할 수도 있습니다.

## Array 생성자로 생성하기

```javascript
var evens = new Array(2, 4, 6, 8);
var empty = new Array();
var a = new Array(2, 4);
var various = new Array(3.14, "pi", true, {x:1, y:2}, [2, 4, 6, 8]);
```

- Array 생성자의 인수가 한 개고 그 값이 양의 정수면 의미가 달라집니다. 이때 인수는 배열 길이를 뜻하므로 배열이 그 길이만큼 생성됩니다.

```javascript
var x = new Array(3);
console.log(x.length) // -> 3
```

- 반면 Array 생성자의 인수가 한 개고 그 값이 양의 정수가 아니면 오류가 발생합니다.

```javascript
var x = new Array(-3)
```

### 배열 요소의 추가와 삭제

```javascript
var a = ["A", "B", "C"];
a[3] = "D";
console.log(a) // -> ["A", "B", "C", "D"];
// push 메서드를 사용하면 요소를 배열 끝에 추가할 수 있습니다.
var a = ["A", "B", "C"];
a.push("D");
console.log(a) // -> ["A", "B", "C", "D"];
// delete 연산자를 사용하면 특정 배열 요소를 삭제할 수 있습니다.
delete a[1];
console.log(a) // -> ["A", undefined, "C", "D"];
// delete 연산자를 사용하여 배열의 요소를 삭제해도 그 배열의 length 프로퍼티 값은 바뀌지 않습니다.
// 즉, 삭제한 요소만 사라집니다.
```

### 희소 배열

- 배열에 요소를 추가하거나 제거하면 인덱스가 0부터 시작되지 않는 배열이 만들어집니다.
- 이러한 배열을 **희소 배열**이라고 부릅니다.

```javascript
var a = ["A", "B", "C"];
a[4] = "E";
console.log(a); // -> ["A", "B", "C", undefined, "E"];
```



- 위 코드를 실행하여 보면 a[3] 이 undefined 라고 표시되지만 실제로 저 요소는 없습니다.
- 이 코드의 배열을 객체 리터럴로 표시하면 다음과 같습니다.
  - { "0": "A", "1": "B", "2": "C", "4": "E"}
- 배열을 객체로 생각하면 희소 배열도 자연스럽게 이해할 수 있습니다.
- 이때 희소 배열의 길이는 배열 요소의 개수보다 큽니다. 반면 희소 배열이 아닌 배열의 길이는 배열 요소의 개수와 같습니다. 