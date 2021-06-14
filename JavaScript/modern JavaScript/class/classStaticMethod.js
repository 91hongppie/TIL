
// constructor가 인수로 받은 name, name 접근자 프로퍼티, _name 프로퍼티는 모두 다른 존재라는 점에 유의
// 정적 메서드를 정의하려면 클래스 멤버 앞에 static 키워드를 붙여줍니다.
class Person {
    // 생성자를 사용한 초기화
    constructor(name) {
        this.name = name;
        Person.personCount++;
    }
    // prototype 메서드
    get name() {
        return this._name;
    }
    set name(value) {
        this._name = value;
    }
    sayName() {
        console.log(this.name);
    }
    // 정적 메서드
    static count() {
        return Person.personCount;
    }
}
Person.personCount = 0;
// personCount에 Person을 호출한 횟수를 기록합니다.
// 정적 메서드 count는 Person.personCount 값을 출력

var person1 = new Person("Tom");
console.log(Person.count());
var person2 = new Person("Huck");
console.log(Person.count());