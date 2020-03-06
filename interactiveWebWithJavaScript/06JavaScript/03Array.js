// length 속성은 배열의 길이를 담고 있다
var brands = ['Apple', 'Coca-Cola', 'Starbucks'];
console.log(brands.length);

// 배열에서 특정 값 찾기
// 문자열에서 썼던 indexOf가 배열에서도 똑같이 동작
// array.indexOf(item)을 하면 array 배열에 item이 포함되어 있는지 확인 가능
// 포함되어 있다면, item이 있는 인덱스가 리턴
// 포함되어 있지 않다면, -1 리턴
// 여러 번 포함되어 있으면, 처음 발견된 인덱스 리턴
console.log(brands.indexOf('Starbucks'));
console.log(brands.indexOf('Kakao'));

// 배열에 값 추가
brands.push('Kakao');
console.log(brands);

brands.push('Samsung', 'LG', 'Facebook');
console.log(brands);

// 배열에서 값 빼기
// array.pop()을 하면 배열 array의 마지막 요소가 배열에서 빠지고, 그 마지막 요소가 리턴
var lastBrand = brands.pop();
console.log(lastBrand);
console.log(brands);

// 배열을 문자열로 바꾸기
// brands.join()
console.log(brands.join());

// 파라미터로 쉼표를 대체할 문자열 넣기
console.log(brands.join('###'));

// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array