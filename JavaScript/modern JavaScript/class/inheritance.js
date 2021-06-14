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

var ellipse = new Ellipse(5, 3);
console.log(ellipse.getArea());
console.log(ellipse.toString());