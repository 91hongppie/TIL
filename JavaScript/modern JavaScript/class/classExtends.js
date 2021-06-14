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
}

var ball = new Ball({x: 0, y:0}, 2);
console.log(ball.toString());   // Circle 중심점 (0,0), 반지름 = 2
console.log(ball.area());       // 12.566370614359172
ball.move(1, 2);
console.log(ball.toString());   // Circle 중심점 (1,2), 반지름 = 2