소프트웨어(프로그램) <- 많은 사람들이 함께 만드는 하나의 거대 구조물

프로그램이 안정적으로, 아름답게 세워지기 위해서는 모두가 따르는 일종의 '룰'이 필요



### 스타일 가이드

문법적인 것 이외에 '어떤 방식과 스타일로 코딩을 하는 게 좋을지' 정해주는 역할

1. 띄어쓰기와 줄바꿈
2. 변수 이름을 짓는 규칙
3. 동작은 하지만 쓰지 말아야  할 코드
4. 그 외 등등..

스타일이 잘 갖추어진 코드는 가독성이 높고, 유지 보수 및 재사용성이 높아지며, 버그를 줄일 수 있는 안정적인 코드가 된다



[에어비엔비]: https://github.com/tipjs/javascript-style-guide
[깃허브에]: https://github.com/rwaldron/idiomatic.js/tree/master/translations/ko_KR
[구글]: https://google.github.io/styleguide/jsguide.html



좋은 이름 <- 보기에 좋고 이해하기 쉽고 실수를 유발하지 않아야 한다



null : 비어있는 값

undefined : 변수에 아무것도 할당되지 않았을 때의 값

자바스크립트에서는 변수의 선언과 초기화를 동시에 하지 않아도 되기 때문에, 선언만 된 변수는 undefined라는 값을 갖게 된다

NaN : Not a Number 숫자가 아닌 것을 숫자로 표현하려 할 때 반환

```javascript
var n = null;
var u;
var num = parseInt('abcd');

console.log(n);  // null
console.log(u);  // undefined
console.log(num);  // NaN
```



#### false 와 true 로 간주되는 것들

자바스크립트의 if문이나 while문의 조건 부분에는 불린이 아닌 다른 자료형의 결과값이 있어도 작동한다

##### 숫자

```javascript
if (0) {
  console.log('0은 true');
} else {
  console.log('0은 false');
}

if (4) {
  console.log('양수는 true');
} else {
  console.log('양수는 false');
}

if (-10) {
  console.log('음수는 true');
} else {
  console.log('음수는 false');
}
```

```
0은 false
양수는 true
음수는 true
```



##### 문자열

```javascript
if ('') {
  console.log('비어있는 문자열은 true');
} else {
  console.log('비어있는 문자열은 false');
}

if ('ab') {
  console.log('안 비어있는 문자열은 true');
} else {
  console.log('안 비어있는 문자열은 false');
}
```

```
비어있는 문자열은 false
안 비어있는 문자열은 true
```



#### null, undefined, NaN

```javascript
if (null) {
    console.log('null은 true');
} else {
    console.log('null은 false');
}

if (undefined) {
    console.log('undefined는 true');
} else {
    console.log('undefined는 false');
}

if (NaN) {
    console.log('NaN은 true');
} else {
    console.log('NaN은 false');
}
```

```
null은 false
undefined는 false
NaN은 false
```



변수 str 이 빈 문자열인지 이렇게 확인 가능

```javascript
if (str) {
  console.log('str은 빈 문자열이 아닙니다.');
} else {
  console.log('str은 빈 문자열입니다.');
}
```



다른 자료형을 불린으로 변형하는 법

비어 있는 문자열은 불린으로 생각했을 때 false

따라서 아래 코드에서 !str 을 하면 true 가 되고, !!str 을 하면 false 가 된다

```javascript
var str = '';
console.log(!str);
console.log(!!str);
```

```
true
false
```



