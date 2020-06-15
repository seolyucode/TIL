console.log('hi');

let sum = 0;
for(const i of [1,2,3]) {
    sum += i;
}

// fetch('GET')
// ajax -> friend 로 바꿔서 생각
const ajax = new XMLHttpRequest()
ajax.open('GET', url)
ajax.send()
ajax.addEventListener('load', function(e) {
    // const ramen = e.target.value;
    // ramen.water()
    // ramen.boil()
    // ramen.eat()
})

while (1) {}

document.querySelector('#aaa')


setTimeout(function () {
    console.log('hi')
}, 1000)
// 타이머에 console.log('hi') 다짐 써서 밖에 보내고 다른일 함.
// (비동기 - non블록킹으로 동작하는.. axios(), XHR(), fetch()등등 인터넷 끊기면 못하는 일들)
// 밖에 나갔다 와야 하는 함수. 인자 중에 하나 함수 써야함.