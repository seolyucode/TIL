// Object 는 Key-Value 로 이루어진 데이터 구조

const endGame = {
    title: '어벤져스: 엔드게임',
    'my-lovers': [
        {name: '아이언맨', actor: '로다주'},
        {name: '헐크', actor: '마크 러팔로'}
    ]
}

console.log(endGame.title)  // 어벤져스: 엔드게임
console.log(endGame['title'])  // 어벤져스: 엔드게임
console.log(endGame["my-lovers"][0].name)  // 아이언맨


// Object Literal (ES6+)

const comics = {
    'DC': ['Aquaman', 'SHAZAM'],
    'Marvel': ['Captain Marvel', 'Avengers']
}
const magazines = null

const bookShop = {
    comics,
    magazines,
}


// method
// 파이썬과 달리 별도의 문법이 있는 것이 아니라 오브젝트의 value에 함수를 할당
const me = {
    name: 'Kim',
    greeting: function(message) {
        return `${this.name} : ${message}`
    }
}

console.log(me.greeting('hi'));  // Kim : hi
console.log(me.name = 'John');  // John
console.log(me.greeting('hello'));  // John : hello


// 앞선 변수/object와 같이 함수도 ES6+ 부터 아래와 같이 선언 가능하다.
const greeting = function(message) {
    return `${this.name} : ${message}`
}

const you = {
    name: 'Yu',
    greeting,
    bye() {
        return 'bye'
    }
}
console.log(you.greeting('hi'));  // Yu : hi
console.log(you.name = 'Jane');  // Jane
console.log(you.greeting('hello'));  // Jane : hello
console.log(you.bye());  // bye


// 메서드 정의시, arrow function 을 사용하지 않는다.