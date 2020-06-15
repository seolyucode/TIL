// length <- 문자열의 길이
var str = 'Codeit';
console.log(str.length);

// 특정 인덱스의 문자 받아오기
// str.charAt(index) 를 하면 문자열 str 의 index 인덱스에 있는 문자를 받아올 수 있다
// str[index]
console.log(str.charAt(2));

// 문자열 안에서 다르 문자열 검색
// str.indexOf(searchValue) 를 하면 문자열 str 내에 문자열 searchValue 가 포함되어 있는지 확인
// 만약 포함되어 있다면, 문자열이 시작되는 문자의 인덱스가 리턴
// 포함되어 있지 않다면, -1 이 리턴
// 여러 번 포함되어 있으면, 처음 발견된 인덱스가 리턴

var str2 = 'Hello World!';
console.log(str2.indexOf('e'));
console.log(str2.indexOf('z'));
console.log(str2.indexOf('ello'));
console.log(str2.indexOf('o'));

// 마지막 인덱스 찾기
// lastIndexOf 는 indexOf 와 동일한데, 가장 뒤에 위치한 검색 결과를 찾아줌
console.log(str2.indexOf('o'));
console.log(str2.lastIndexOf('o'));

// 대소문자 변환
// str.toUpperCase() 를 하면 str 의 모든 글자가 대문자로 바뀌어서 리턴
console.log(str.toUpperCase());

// str.toLowerCase() 를 하면 str 의 모든 글자가 소문자로 바뀌어서 리턴
console.log(str.toLowerCase());

// 문자열 자르기
// 시작 지점과 끝 지점으로 자르기
// str.substring(indexStart, indexEnd) 를 하면 인덱스 indexStart 부터 인덱스 indexEnd 전까지의 문자열을 잘라서 새로운 문자열 리턴
// indexEnd 쓰지 않으면, indexStart 부터 끝까지 문자열이 잘림
console.log(str.substring(2, 5));
console.log(str.substring(2));

// 시작 지점과 길이로 자르기
// str.substr(start, length) 를 하면 인덱스 start 부터 길이 length 의 문자열이 잘려서 리턴
console.log(str2.substr(2, 5));

// 앞뒤의 공백 없애기
// str.trim() 을 하면 문자열 str 의 앞뒤로 있는 '공백(띄어쓰기, 들여쓰기, 줄바꿈 등)'을 모두 지운 새로운 문자열이 리턴
var str3 = '    Hello World!    ';
console.log(str3.trim());