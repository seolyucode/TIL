var i = 100;

while (true) {
    // i가 23의 배수면 반복문을 끝냄
    if (i % 23 == 0) {
        // while문의 조건부분과 상관 없이 반복문에서 나오고 싶으면 break문
        break;
    }
    i = i + 1;
}

console.log(i);


var j = 0;

while (j < 15) {
    j = j + 1;

    // i가 홀수면 console.log(i) 안하고 바로 조건부분으로 돌아감
    if (j % 2 == 1) {
        // 현재 진행되고 있는 수행부분을 중단시키고 바로 조건부분을 다시 확인하고 싶으면 continue문
        continue;
    }
    console.log(j);
}