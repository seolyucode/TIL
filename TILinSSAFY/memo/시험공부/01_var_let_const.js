// 변수 var, let, const
/*
1. 자바스크립트에서는 기본적으로 변수를 선언해야 한다.
2. ES6 이전에는 var 를 이용했으나 우리는 const 를 중심으로 사용하고, let 은 필요한 경우에만 사용
*/

// var 는 function 스코프
// let, const 는 block 스코프


console.log('var 는 function 스코프')
for(var j=0; j<1; j++) {
    console.log(j)  // 0
}
console.log(j)  // 1


console.log('let 은 block 스코프')
for(let i=0; i<1; i++) {
    console.log(i)
}
// console.log(i)  // i is not defined


console.log('const 는 block 스코프')
console.log('let은 재할당이 자유로우나 const는 재할당이 금지된다.')
console.log('const는 반드시 선언과 동시에 할당이 이루어져야 한다')
// for(const k=0; k<1; k++) {
//     console.log(k)
// }
// console.log(k)  // TypeError: Assignment to constant variable.


console.log('함수 스코프 - var')
const myFunction = function() {
    for(var k=0; k<1; k++) {
        console.log(k)
    }
    console.log(k)
}
myFunction()
// 0
// 1
// console.log(k)  //  k is not defined


console.log('var 는 재선언이 가능하지만 let, const 는 재선언 불가능')
var a = 1
var a = 2

let b = 1
// let b = 3  // Uncaught SyntaxError: Identifier 'b' has already been declared

const c = 1
// const c = 4  // Uncaught SyntaxError: Identifier 'c' has already been declared

console.log('let 은 재할당이 가능하지만, const 는 불가능')
let d = 3
d = 5

const e = 5
// e = 3  // Uncaught TypeError: Assignment to constant variable.

// 따라서, const 는 선언시 반드시 할당이 필요하다.
// const f  // Uncaught SyntaxError: Missing initializer in const declaration

let g
g = 3


console.log('위의 변수 선언 키워드를 사용하지 않으면 함수/블록 안에서 선언되더라도 무조건 전역 변수로 취급됨')

function myFunction1 () {
    for(p=0; p<1; p++) {
        console.log(p)
    }
    console.log(p)
}
myFunction1()
// 0
// 1
console.log(p)  // 1
// console.log(window.p)  // ReferenceError: window is not defined

console.log('따라서, 무조건 변수 선언 키워드를 작성하고 const 를 기본적으로 쓰고, let 을 사용해야 하는 상황에 한하여 변경')