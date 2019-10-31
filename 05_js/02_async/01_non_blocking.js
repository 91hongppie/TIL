// function sleep_3s() {
//     setTimeout(() => console.log('wake up'), 3000)
// }
// console.log('알파')
// sleep_3s()
// console.log('오메가')


// function first() {
//     console.log('first')
// }

// function second() {
//     console.log('second')
// }

// function third() {
//     console.log('third')
// }

// first()
// setTimeout(second, 1000)
// third()


console.log('하이')
setTimeout(function ssafy() {
    console.log('싸피')
}, 5000)
console.log('바이')

function printHello() {
    console.log('hello from baz')
}

function baz() {
    setTimeout(printHello, 3000)
}

function bar() {
    baz()
}

function foo() {
    bar()
}

foo()