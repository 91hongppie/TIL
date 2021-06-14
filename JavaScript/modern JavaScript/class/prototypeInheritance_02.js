// 이 방법은 Circle.prototype에 이미 생성된 Ellipse의 프로퍼티를 낭비하는 단점이 있다.
function Ellipse(a, b) {
    this.a = a;
    this.b = b;
}
Ellipse.prototype.getArea = function() {
    return Math.PI*this.a*this.b;
}
Ellipse.prototype.toString = function() {
    return "Ellipse " + this.a + " " + this.b;
}

function Circle(r) {
    this.a = r;
    this.b = r;
}

Circle.prototype = new Ellipse();
Circle.prototype.constructor = Circle;

var circle = new Circle(2);

console.log(circle.getArea());
console.log(circle.toString());