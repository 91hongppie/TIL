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

// Ellipse.prototype 을 Circle.prototype에 상속한다.
Circle.prototype = Object.create(Ellipse.prototype, {
    constuctor: {
        configurable: true,
        enumerable: true,
        value: Circle,
        writable: true
    }
});

Circle.prototype.toString = function() {
    return "Circle " + this.a + " " + this.b;
};

var circle = new Circle(2);
console.log(circle.getArea());
console.log(circle.toString());