function factorial(num) {
    var factorialValue = 1;
    // 코드를 작성하세요.
    while(num >= 1) {
        factorialValue *= num;
        num--;
    }
  
    return factorialValue;
}

function factorial2(n) {
    var result = 1;

    for (var i = 1; i <= n; i++) {
        result = result * i;
    }
    return result;
}

// 테스트 코드
console.log(factorial(10));
console.log(factorial(5));
console.log(factorial(3));
console.log(factorial(0));

console.log(factorial2(10));
console.log(factorial2(5));
console.log(factorial2(3));
console.log(factorial2(0));