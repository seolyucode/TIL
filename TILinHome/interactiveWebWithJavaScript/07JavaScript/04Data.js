// 날짜와 관련된 프로그램을 짜고 싶으면, Data 객체 활용

// 현재 날짜로 설정
// 파라미터 없이 new Data() 를 하면 
// 현재 날짜로 설정되어 있는 Data 객체가 생성돼서 리턴

var date0 = new Date();

// 원하는 날짜로 설정
// 파라미터를 써주면 원하는 날짜로 설정 가능
// 날짜만 쓸 경우, 0시 0분 0초로 지정
var date1 = new Date('June 11, 1988 05:25:30');
var date2 = new Date('1988-06-11T05:25:30');

var date3 = new Date('1999-12-15');
var date4 = new Date('12/15/1999');
var date5 = new Date('December 15 1999');
var date6 = new Date('Dec 15 1999');

// 날짜 정보 받아오기
var date = new Date('June 11, 1988 05:25:30');

console.log(date.getFullYear());
// getMonth()는 0부터 시작하기 때문에
// 2는 3월을 의미
console.log(date.getMonth());
console.log(date.getDate());
// getDay()는 날짜가 아니라 요일을 리턴
// 0 일요일 3 수요일
console.log(date.getDay());
console.log(date.getHours());
console.log(date.getMinutes());
console.log(date.getSeconds());
console.log(date.getMilliseconds());
console.log(date.toString());
console.log(date.toLocaleString());
console.log(date.toLocaleDateString());
console.log(date.toLocaleTimeString());

// getTime() 메서드는 1970년 1월 1일 자정으로부터 몇 ms가 지났는지 알려줌
var date7 = new Date('June 11, 1988 05:25:30');
console.log(date7.getTime());

// 이 ms 값에 나눗셈을 적절히 사용하면 초, 분, 시, 일 등의 단위로 변환 가능
console.log(date7.getTime() + 'ms');
console.log(date7.getTime()/1000 + '초');
console.log(date7.getTime()/1000/60 + '분');
console.log(date7.getTime()/1000/60/60 + '시간');

// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/prototype