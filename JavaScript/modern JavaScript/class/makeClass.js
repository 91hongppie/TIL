// 함수 선언문으로 정의하는 방법
function Card(suit, rank) {
    this.suit = suit;
    this.rank = rank;
};
Card.prototype.show = function() {
    console.log(this.suit + this.rank);
};
// 함수 리터럴로 정의하는 방법
var Card = function(suit, rank) {
    this.suit = suit;
    this.rank = rank;
};
Card.prototype.show = function() {
    console.log(this.suit + this.rank);
};
// 클래스 선언문으로 정의하는 방법
class Card {
    constructor (suit, rank) {
        this.suit = suit;
        this.rank = rank;
    }
    show() {
        console.log(this.suit + this.rank);
    }
}

// 클래스 표현식으로 정의하는 방법
var Card = class {
    constructor (suit, rank) {
        this.suit = suit;
        this.rank = rank;
    }
    show() {
        console.log(this.suit + this.rank);
    }
};