// if - else if - else
const n = 15;

if(n%3==0) {
    console.log('n은 3의 배수');
} else if(n%5==0) {
    console.log('n은 5의 배수');
} else {
    console.log('n은 3의 배수도 아니고, 5의 배수도 아니다');
}
// n은 3의 배수

// while - for - for of
while(true) {
    console.log('안녕하세요');
    if (Math.random()*100 > 90) {
        break;
    }
}

for (let i=0; i<5; i++) {
    console.log('안녕하세요', i);
}

// for of - iterable
for (const i of [1, 2, 3]) {
    console.log(i);
}
// 1
// 2
// 3


// == vs ===
