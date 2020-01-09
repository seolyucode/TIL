Why JavaScript?

Front-End 일 하려면 자바스크립트

Fragmentation

자바스크립트는 웹에서 쓸 수 있는 단하나의 언어. 단점이 많지만 자바스크립트 할 줄 아는 프로그래머는 할 게 많다.

자잘한 이벤트들을 두개 이상 할 수 있게 해주고 영향력 강해지고 있음.

많은 것을 해낼 수 있게 함.

웹 앱, 웹 사이트, 모바일 어플리케이션, 비디오 게임, 데스크톱 앱 등 만들 수 있음

VS Code 나 Atom <- JS로 만들어짐

모든 컴퓨터가 이해함.



ex) world draw



자바스크립트

ECMAScript <- Specification 명칭

ES5 = ECMAScript5



바닐라 자바스크립트 <- 라이브러리 없는  날 것의 자바스크립트



커피스크립트?



컨셉 <- Function, Variable, 조건, 이벤트, class, objects, arrays ..

 

변수 variable

변경되거나 변경될 수 있는 것

a모든 expressions, instructions 한줄에;

```javascript
Create
Initialize
Use
```

```javascript
let a = 33;
let b = a - 5;
a = 3;  // 업데이트
console.log(b, a);  // 28 3
```



```javascript
const a = 10;  // const 상수. 안변함
let b = a - 5;
a = 4;  //  Assignment to constant variable. 상수 변수에 대입.
console.log(b, a);
```



```javascript
/* String
const what = "Seolyu";
*/

/* true 는 텍스트가 아님 Boolean
const wat = true;
*/

/* Number
const what = 666;
*/

/* Float
const wat = 55.1;
*/
```



```javascript
const monday = "Mon";
const tue = "Tue";
const wed = "Wed";
const thu = "Thu";
const tri = "Fri";

console.log(monday, tue, wed, thu, fri);

// camel case
// lowerOfWeek
```

```javascript
const something = "Something"

const daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", true, 4, something];

console.log(daysOfWeek);
console.log(daysOfWeek[2]);
```



Object 에는 각 value 에 이름을 줄 수 있음

```javascript
const seolyuInfo = ["Seolyu", "55", true, "Seoul"];

console.log(nicoInfo[0]);
```

```javascript
const seolyuInfo = {
    name: "Seolyu",  // name 은 변수
    age: 55,
    gender: "Female",
    isHandsome: true,
    favMovies: ["Along the gods", "LoTR", "Oldboy"],
    favFood: [
        {
            name:"Kimchi",
            fatty: false
        }, 
        {
            name:"Cheese burger", 
            fatty: true
        }
    ]
}

seolyuInfo.age = 44;

console.log(seolyuInfo);
console.log(seolyuInfo.gender);
```

데이터를 정렬

Array <- DB에서 가져온 리스트 데이터

Object <- 

 

```javascript
console.log(seolyuInfo.gender);
// console 은 object
// log 라는 키. 함수
```

```javascript
console.log(console);
```

내장함수(built-in function)



함수? 기능. 코드 조각. 원하는 만큼 쓸 수 있는 코드

```javascript
console.log('Grettings Jun')
console.log('Hello Liyn')
console.log('Hello Dal')
console.log('Hello Seolyu')
```

```javascript
function sayHello(potato) {
    console.log('Hello!', potato);
}

sayHello("Seolyu");
console.log("Hi!");
```

인자(argument)

argument는 변수

위 코드에서 potato 는 parameter 혹은 argument 함수 안에서 사용하게 될 이름.

"Seolyu" 값을 potato라는 것에 넣음

외부에 있는 데이터를 읽는 함수를 만들기

함수에게 외부에 있는 데이터를 주는 방법



console.log(arg1, arg2);

```javascript
function sayHello(potato, chicken) {
    console.log('Hello!', potato, " you have ", chicken, " years of age.");
}

sayHello("Seolyu", 16);
```

console.log 함수는 argument를 무한히 가질 수 있다.

sayHello 함수는 2개 argument 뿐이다.



```javascript
function sayHello(name, age) {
    console.log(`Hello ${name} you are ${age} years old`);
}

// greetSeolyu는 sayHello 함수의 리턴값 
const greetSeolyu = sayHello("Seolyu", age)

console.log(greetSeolyu)  // undefined
```

```javascript
function sayHello(name, age) {
    return `Hello ${name} you are ${age} years old`;
}

// greetSeolyu는 sayHello 함수의 리턴값 
const greetSeolyu = sayHello("Seolyu", age)

console.log(greetSeolyu)
// console.log 는 객체

const calculator = {
    plus: function(a, b) {
        return a + b;
    }
}

const plus = calculator.plus(5, 5)
console.log(plus)
```



DOM <- Document Object Module

자바스크립트는 html에 있는 모든 요소를 가지고 와서 DOM 객체로 바꿈

객체는 많은 키를 가지고 있다



