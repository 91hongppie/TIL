function Person(name) {
    Object.defineProperty(this, "name", {
        get: function () {
            return name;
        },
        set: function(newName) {
            name = newName;
        },
        enumerable: true,
        configurable: true
    });
}
Person.prototype.sayName = function() {
    console.log(this.name);
};

var person = new Person("Tom");
console.log(person.name)
person.name = "Huck";
console.log(person.name);
person.sayName();