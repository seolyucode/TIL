// 절댓값 (Absolute Number)

// 절댓값(absolute value)
// 어떤 값의 '양수(positive number)' 버전
// Math.abs(x) <- x의 절댓값이 리턴

console.log(Math.abs(-10));
console.log(Math.abs(10));

// 최댓값 (Maximum)
// Math.max 함수에 파라미터로 여러 수를 넘겨주면, 그 중 가장 큰 값이 리턴
console.log(Math.max(2, -1, 4, 5, 0));

// 최솟값 (Minimum)
// Math.min 함수에 파라미터로 여러 수를 넘겨주면, 그 중 가장 작은 값이 리턴
console.log(Math.min(2, -1, 4, 5, 0));

// 거듭제곱 (Exponentiation)
console.log(Math.pow(2, 3));
console.log(Math.pow(5, 2));

// 제곱근 (Square Root)
console.log(Math.sqrt(25));
console.log(Math.sqrt(49));

// 반올림 (Round)
console.log(Math.round(2.3));
console.log(Math.round(2.4));
console.log(Math.round(2.49));
console.log(Math.round(2.5));
console.log(Math.round(2.6));

// 버림과 올림 (Floor and Ceil)
console.log(Math.floor(2.4));
console.log(Math.floor(2.49));
console.log(Math.floor(2.8));
console.log('-');
console.log(Math.ceil(2.4));
console.log(Math.ceil(2.49));
console.log(Math.ceil(2.8));

// 난수 (Random)
// Math.random 을 하면 0 이상 1 미만의 값이 랜덤으로 리턴
console.log(Math.random());
console.log(Math.random());
console.log(Math.random());
console.log(Math.random());

// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math