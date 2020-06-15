// ES6+ 에서는 key - value 에 같은 단어 쓸 때 축약할 수 있다

// ES5
var books = ['Learning JS', 'Eloquent JS'];

var comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

var magazine = {}

var bookshop = {
    books: books,
    comics: comics,
    magazine: magazine,
}

// ES6+
const books = ['Learning JS', 'Eloquent JS'];

const comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

const magazine = {}

const bookshop = {
    books,  // books: books, 를 줄여서 한 번만 작성 
    comics, 
    magazine,
}

// Method(객체 안의 함수)
// 절대 arrow function () => {} 쓰지 말자.
// method : function
// this => me

// method: () => {}
// this => window

const me = {
    name: 'seolyu',
    // 메서드 정의
    greet: function() {
        console.log(this)
        return `Hello, I'm ${this.name}`
    },
    walk: () => {
        console.log(this)
        return `${this.name} is walking..`
    }
};

/*
Article.objects.get(title='hi')  // 처음 하나만
Article.objects.filter(title='hi')  // zero부터 전부
*/