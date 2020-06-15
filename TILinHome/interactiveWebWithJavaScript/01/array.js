// var brands = ['Apple', 'Coca-Cola', 'Starbucks'];

// var iPad = [800, 'Black', true];

// console.log(typeof brands);
// console.log(typeof iPad);

// console.log(brands[1]);

// var text1 = 'Hello';
// console.log(text1[0]);
// console.log(text1[1]);

// var text2 = ['H', 'e', 'l', 'l', 'o'];
// console.log(text2[0]);
// console.log(text2[1]);

// var text1 = 'Hello';
// var text2 = ['H', 'e', 'l', 'l', 'o'];
// console.log(text1.length);
// console.log(text2.length);

// console.log(typeof text1);
// console.log(typeof text2);

// console.log(text1 == text2);

// 배열은 mutable
var text1 = ['h', 'e', 'l', 'l', 'o'];
text1[0] = 'b';
console.log(text1);

// 문자열은 immutable
var text2 = 'hello';
text2[0] = 'b';
console.log(text2);