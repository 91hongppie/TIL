
// function을 이용한 표현
function Circle(center, radius) {
    this.center = center;
    this.radius = radius;
}

Circle.prototype.area = function() {
    return Math.PI*this.radius*this.radius;
}

// class를 이용한 표현
/* 
    class 키워드 뒤에 생성자 함수의 이름을 표기
    { ... } 안은 클래스 몸통(class body), 클래스 몸통에는 클래스 멤버를 정의. 
    클래스 멤버는 함수 선언문에서 function 키워드를 생략한 표현식.
    constructor() {...} 는 생성자로 객체를 생성할 때 초기화 처리를 담당하는 메서드.
    constructor 다음에 작성된 클래스 멤버는 생성자 함수의 prototype에 메서드로 추가.
*/
/*
    클래스 선언문과 함수 선언문의 차이
    1. 클래스 선언문은 끌어올리지 않습니다.
    2. 클래스 선언문은 한번만 작성할 수 있습니다. 
       같은 이름을 가진 클래스 선언문을 두 번 이상 작성하면 타입 오류 발생
    3. 클래스 선언문에 정의한 생성자만 따로 호출할 수 없습니다.
*/
class Circle {
    // 생성자를 사용한 초기화
    constructor(center, radius) {
        this.center = center;
        this.radius = radius;
    }
    // prototype 메서드
    area() {
        return Math.PI*this.radius*this.radius;
    }
};

var c = new Circle({x: 0, y: 0}, 2);
console.log(c.area());


// 클래스 표현식으로도 정의할 수 있습니다.
var Circle = class {
    constructor(center, radius) {
        this.center = center;
        this.radius = radius;
    }
    area() {
        return Math.PI*this.radius*this.radius;
    }
};

// class 다음에는 모든 식별자를 이름으로 사용할 수 있습니다.
// 단, 이렇게 표기한 이름(아래의 경우 kreis)은 클래스 몸통 안에서만 유효합니다.
// var Circle = class kreis { ... };