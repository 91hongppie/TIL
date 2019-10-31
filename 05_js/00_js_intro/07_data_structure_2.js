const me = {
    name: 'ssafy',
    'phone number': '01012345678', // key 가 여러단어 일 때
    appleProduct: {
        applewatch: 'series3',
        iphone: 'xs',
        macbook: '2017pro'
    }
}

console.log(me.name)
console.log(me['name'])
console.log(me['phone number'])
console.log(me['appleProduct']['iphone'])

// Object Literal (객체 표현법)
var books = ['Learning JS', 'Eloquent JS']

var comics = {
    'DC': ['Joker', 'Aquaman'],
    'Marvel': ['Captain Marvel', 'Avengers']
} // 객체

var magazines = null

var bookShop = {
    books: books,
    comics: comics,
    magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// ES6+
// object 의 key와 value가 같다면, 마치 배열처럼 한번만 작성 가능
var bookShopTwo = {
    books,
    comics,
    magazines
}
console.log(bookShopTwo)

// JSON
const jsonData = JSON.stringify({ // JSON -> String
    coffee: 'Americano',
    iceCream: 'Mint Choco,'
})
console.log(jsonData)
console.log(typeof jsonData)

const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)