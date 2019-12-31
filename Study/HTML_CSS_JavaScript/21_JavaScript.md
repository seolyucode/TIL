서버 쪽에서도 자바스크립트를 실행할 수 있게 되었다 api 개발할 때 nodejs통해 자바스크립트 쓸 수 있게 됨

electronjs.org 이 프레임워크로 데스크탑 어플리케이션 만들 수 있고

nativescript와 reactnative로 웹/모바일 어플리케이션 만들 수 있다.

하드웨어에서도 nodejs 통해 자바스크립트 사용할 수 있어서 Iot에서도 사용됨



http://learnjs.vlpt.us/basics/



개발자도구 Console 에서

console.log('Hello JavaScript!');

console.log(1+2+3+4);

https://codesandbox.io/

create sandbox - vanilla 에서도 console

크롬에서 상단에 CodeSandbox 설치하면 새로운 창으로 작업할 수 있음



## 변수와 상수

```javascript
// 변수선언 let 은 값을 바꿀 수 있음
// 변수 선언 후 똑같은 이름 안됨
let value = 1;
console.log(value);

value = 2;
console.log(value);
```

```javascript
// 상수. 값 바꿀 수 없음
const a = 1;
```

```javascript
// var 는 똑같은 이름으로 여러번 선언 가능
var a = 1;
var a = 2;
```

```javascript
let text = 'hello';
let name = "헬로우 자바스크립트";
```

.prettierrc 설정 때문에 ; 랑 " " 

```javascript
// boolean 은 참 or 거짓만 표현
let good = true;
let loading = false;
```

```javascript
let good = null; // 없다
let something = undefined; // 아직 정해지지 않았다
```

```javascript
let friend = null;
let criminal;
console.log(criminal); // undefined
```



## 연산자

```javascript
let a = 1 + 2 - (3 * 4) / 4;
console.log(a); // 0
console.log(a--); // 0
console.log(a); // -1

let b = 1;
console.log(b++); // 1
console.log(b); // 2
console.log(++b); // 3
console.log(b); // 3
```

```javascript
let a = 1;
a += 3;
a -= 3;
a *= 3;
a /= 3;
console.log(a);
```



## 논리 연산자

```javascript
// NOT !
// AND &&
// OR ||

const a = !true;
console.log(a);

const b = true && true; // 모두 true 일 때 true
console.log(b);

const c = true || false; // 둘 중 하나라도 true 면 true
console.log(c);
```

```javascript
// 우선순위대로
// NOT !
// AND &&
// OR ||

const a = !true;
console.log(a);

const b = true && true; // 모두 true 일 때 true
console.log(b);

const c = true || false; // 둘 중 하나라도 true 면 true
console.log(c);

const value = !((true && false) || (true && false) || !false);
// !(true && false || true && false || true)
// !(false || false || true)
// !(true)
// false

console.log(value);
```



## 비교연산자

```javascript
const a = 1;
const b = 1;
const equals = a === b; // 두 값 비교 ===
console.log(equals);

const c = false;
const d = 0;
const equals2 = c == d; // == 는 타입을 비교안함
console.log(equals2);

const e = null;
const f = undefined;
const equals3 = e == f;
console.log(equals3);

const g = 1;
const h = "1";
const notEquals = g !== h;
const notEquals2 = g != h;
console.log(notEquals);
console.log(notEquals2);
```

```javascript
const a = 10;
const b = 15;
const c = 15;

console.log(a < b);
console.log(b > a);
console.log(b >= a); // = 이 뒤에 옴
console.log(a <= c);
console.log(b < c);
```

```javascript
const a = "안녕";
const b = "하세요";

console.log(a + b); // 안녕하세요
```



## 조건문

```javascript
const a = 1;
if (a + 1 === 2) {
  const a = 2;
  console.log("if문 안의 a 값은 " + a); // 2
  console.log("a + 1 이 2 입니다.");
  console.log("blabla");
}
console.log("if문 밖의 a 값은 " + a); // 1
```

```javascript
const a = 10;
if (a > 15) {
  console.log("a가 15보다 큽니다.");
} else {
  console.log("a가 15보다 크지 않습니다.");
}
```

```javascript
const a = 10;

if (a === 5) {
  console.log("5 입니다!");
} else if (a === 10) {
  console.log("10 입니다!");
} else {
  console.log("5도 아니고 10도 아닙니다.");
}
```



## Switch Case

```javascript
const device = "iphone";

switch (device) {
  case "iphone":
    console.log("아이폰!");
    break;
  case "ipad":
    console.log("아이패드!");
    break;
  case "galaxy note":
    console.log("갤럭시 노트!");
    break;
  default:
    console.log("모르겠네요");
}
```



## 함수

```javascript
function add(a, b) {
  return a + b;
}

const sum = add(1, 2);
console.log(sum); // 3
```

```javascript
function hello(name) {
  console.log("Hello, " + name + "!");
}

hello("Seolyu");
```

