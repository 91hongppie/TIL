// 슈퍼 타입의 메서드 이용하기

function Ellipse(a, b) {
    this.a = a;
    this.b = b;
};

Ellipse.prototype.getArea = function() {
    return Math.PI*this.a*this.b;
};

Ellipse.prototype.toString = function() {
    return "Ellipse " + this.a + " " + this.b;
};

function Circle(r) {
    // Ellipse 생성자를 빌려와서 프로퍼티를 정의합니다.
    Ellipse.call(this, r, r);
    // 이곳에서 새로운 프로퍼티를 작성하거나 기존의 프로퍼티를 덮어쓸 수 있습니다.
}

Circle.prototype = Object.create(Ellipse.prototype, {
    constructor: {
        configurable: true,
        enumerable: true,
        value: Circle,
        writable: true
    }
});

// 슈퍼 타입의 toString 메서드를 이용해서 Circle.prototype.toString을 정의합니다.
Circle.prototype.toString = function() {
    var str = Ellipse.prototype.toString.call(this);
    return str.replace("Ellipse", "Circle");
}

var circle = new Circle(2);

console.log(circle.getArea());
console.log(circle.toString());