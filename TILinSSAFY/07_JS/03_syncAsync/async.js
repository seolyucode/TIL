// JS: Non-Blocking

// function sleep_3s() {
//     setTimeout(() => {console.log('Wake Up!')}, 3000);
// }

// console.log('Start sleeping');
// sleep_3s();
// console.log('End of program');

// 그럼 어떤 함수/작업들이 Non blocking 한가용?
/*
    지금 당장 해결할 수 없고
    결과도 확신 할 수 없는 모든 일
*/

function complexTask() {
    console.log('start');
    for(let i=0; i<1000000000; i++) {}
        console.log('오래걸림');
}

setTimeout(() => {console.log('짱빨리끝남!')}, 1)  // 불확실
complexTask()  // 확실