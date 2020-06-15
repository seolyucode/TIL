var a = 100;
console.log(a);

function foo() {
    console.log('안녕하세요');
}

foo();

// 요즘엔 var 안쓰고 let, const
let b = 100;
console.log(b);

// const(상수)는 값을 바꿀 수 없다
const c = 100;
console.log(c);

// var 는 변수의 유효 범위(scope)가 함수
// 방 안에서는 밖에 있는 애를 알 수 있고
// 밖에서는 안에 있는 애 모름

// const 는 블록단위
// var 는 되지만 let 과 const 는 유효범위 {블록단위} 라서 안됨
if (true) {
    var d = 100;
}

console.log(d);