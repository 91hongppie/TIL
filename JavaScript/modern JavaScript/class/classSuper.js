class Circle {
    constructor(center, radius) {
        this.center = center;
        this.radius = radius;
    }
    area() {
        return Math.PI*this.radius*this.radius;
    }
    toString() {
        return "Circle "
            + "중심점 (" + this.center.x + "," + this.center.y
            + "), 반지름 = " + this.radius;
    }
}


// extends 키워드를 클래스 선언문이나 클래스 표현식에 붙여 주면 다른 생성자를 상속받을 수 있습니다.
class Ball extends Circle {
    move(dx, dy) {
        this.center.x += dx;
        this.center.y += dy;
    }
    // super 키워드를 활용하면 서브 타입의 생성자가 슈퍼 타입 생성자의 메서드를 호출할 수 있습니다.
    toString() {
        var str = super.toString();
        return str.replace("Circle", "Ball");
    }
}

var ball = new Ball({x:0, y:0}, 2);
console.log(ball.toString());   // Ball 중심점 (0,0), 반지름 = 2