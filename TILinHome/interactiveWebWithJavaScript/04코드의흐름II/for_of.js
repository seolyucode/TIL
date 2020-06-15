var brands = ['NIKE', 'ADIDAS', 'REEBOK'];

// for (var i = 0; i < 3; i++) {
//     console.log(brands[i]);
// }

for (value of brands) {
    console.log(value);
}

var arr =  ['Americano', 'Latte', 'Tea'];

// for...of
for (var v of arr) {
  console.log(v);
}

console.log('---');

// for...in
for (var k in arr) {
  console.log(k);
}

// for...in
for (var k in arr) {
    console.log(arr[k]);
  }