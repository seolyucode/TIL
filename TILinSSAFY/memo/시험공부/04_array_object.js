const numbers = [1, 2, 3, 4];

console.log(numbers[0]);  // 1
console.log(numbers[-1]);  // undefined. 정확한 양의 정수 index 만 가능
console.log(numbers.length);  // 4

console.log(numbers.reverse());  // [ 4, 3, 2, 1 ]
console.log(numbers);  // [ 4, 3, 2, 1 ]


// push() 배열의 끝에 아이템을 추가
console.log(numbers.push('a'));  // 5 (new length)
console.log(numbers);  // [ 4, 3, 2, 1, 'a' ]


// pop() 배열의 마지막 아이템을 제거
console.log(numbers.pop());  // a  
console.log(numbers);  // [4, 3, 2, 1]


// unshift() 배열의 앞에 아이템을 추가
console.log(numbers.unshift('a'));  // 5 (new length)
console.log(numbers);  // [ 'a', 4, 3, 2, 1 ]


/* 복사본 or 다른 값 return */
// includes() 메서드는 배열이 특정 요소를 포함하고 있는지 판별 
console.log(numbers.includes(1));  // true
console.log(numbers.includes(0));  // false
console.log(numbers.includes(3));  // true

console.log(numbers.push('a'));  // 6
console.log(numbers.push('a'));  // 7
console.log(numbers);  // [ 'a', 4, 3, 2, 1, 'a', 'a' ]

console.log(numbers.indexOf('a'));  // 0  <= 처음 찾은 요소의 index
console.log(numbers.indexOf('b'));  // -1  <= 없으면 -1

console.log(numbers.join());  // a,4,3,2,1,a,a
console.log(numbers.join(''));  // a4321aa
console.log(numbers.join('-'));  // a-4-3-2-1-a-a

console.log(numbers);  // [ 'a', 4, 3, 2, 1, 'a', 'a' ]

console.log(typeof numbers)  // object
console.log(typeof(numbers))  // object