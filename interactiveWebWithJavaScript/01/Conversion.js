var scoreString = '10';

Number(scoreString);

console.log(typeof scoreString);
console.log(typeof Number(scoreString));
console.log(typeof String(20));

// var favoriteNumber = window.prompt("가장 좋아하는 숫자를 적어주세요.");
// window.prompt 는 입력값을 문자열로 받아서
// typeof favoriteNumber; 해보면 "string"
// var favoriteNumber = Number(window.prompt("가장 좋아하는 숫자를 적어주세요."));
// typeof favoriteNumber; 해보면 "number"

// Number("hello"); 해보면 NaN 숫자가 아니다