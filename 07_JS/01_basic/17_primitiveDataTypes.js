// 17_primitiveDataTypes.js

typeof true;  // boolean // typeof는 함수가 아님
typeof false;  // boolean

// 없다. 확실히 없다. 의도함
typeof null;  // object
// 아 몰라.. 없어.. 의도하지 않음
typeof undefined;  // undefined

[1,2,3][100]  // undefined
({a: 1}).b  // undefined

typeof 'asdf';  // string
typeof 1;  // number
typeof 1.1;  // number
typeof Infinity;  // number
typeof NaN;  // number

typeof [1,2];  // object 배열도 object
Array.isArray([1,2])  // true
typeof {a:1, b:2};  // object

typeof function(){};  // function

typeof {};  // object
typeof [];  // object

// 함수 <- 함수자체
// 메서드 <- 주어가 있어야 함. 객체에 종속되어있는 함수  객체.함수
[1,2].reverse()

// 객체 선언 (ssafyStd <- 객체)
const ssafyStd = {
    name: 'yu',
    classNo: 3,
    greet: function() {
        console.log('hi')
    }
}

ssafyStd.name
ssafyStd.classNo
ssafyStd.greet()

// 파이썬과 달리 자바스크립트는 중괄호 key-value 객체

function a (x) {
    console.log(x)
}
// undefined

a()
// undefined