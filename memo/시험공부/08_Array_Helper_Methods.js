var fruits = ['apple', 'banana', 'peach'];

for(var i=0; i<fruits.length; i++) {
    console.log(fruits[i]);
}

// apple
// banana
// peach


// 위 코드를 forEach 메소드로 다시 구현해보면
fruits.forEach(function(fruit) {
    console.log(fruit);
});


// map
var juice = [];

for(var i=0; i<fruits.length; i++) {
    juice.push(fruits[i]+'juice');
}

var juice = fruits.map(function(fruit) {
    return fruit + ' juice';
});
console.log(juice);

var juice2 = fruits.map(fruit => `${fruit} juice`);
console.log(juice2);


// filter
var datas = [
    {id:3, type:'comment', content: '굿모닝'},
    {id:6, type:'post', content: '좋은 아침이네요'},
    {id:10, type:'comment', content: '좋은 아침'},
    {id:1, type:'post', content: '안녕하세요'},
];

var filteredData = [];
for(var i=0; i<datas.length; i++) {
    if(datas[i].type === 'post') {
        filteredData.push(datas[i]);
    }
}
console.log(filteredData)

var filteredData2 = [];
var filteredData2 = datas.filter(data => {
    return data.type == 'post';
});
console.log(filteredData2)


// find
var ret = datas.find(data => {
    return data.id === 10;
});
console.log(ret);


// every
var scores = [
    { subject: '국어', point: '100'},
    { subject: '영어', point: '90'},
    { subject: '수학', point: '80'},
    { subject: '컴퓨터', point: '10'}
];

var pass = true;

var pass = scores.every(score => {
    return score.point > 70;
});
console.log(pass);


// some
var pass = scores.some( score => {
	return score.point > 70;
});
console.log(pass);


// reduce: