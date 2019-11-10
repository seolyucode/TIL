// 함수 선언식
function myFunc1 (name) {
    console.log('happy hacking')
    console.log(`welcome, ${name}`)
}


// 함수 표현식
const myFunc2 = function (name) {
    console.log('happy hacking')
    console.log(`welcome, ${name}`)
}

console.log(typeof myFunc1)  // function
console.log(typeof myFunc2)  // function


// 화살표 함수 (ES6+)
// 주의, 화살표 함수의 경우 function 키워드로 정의한 위의 함수와
// 100% 동일한 것이 아님
const myFunc3 = (name) => {
    console.log('happy hacking')
    console.log(`welcome, ${name}`)
}

console.log(typeof(myFunc3))  // function


// syntactic sugar 와 관련되 내용
// return 문이 한 줄 일 때 / 인자가 없을 때 / 인자가 하나일 때 등

