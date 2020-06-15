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

 

```javascript
alert('Im Working. Im JS. Im Beautiful. Im worth it')
```



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



```javascript
// console.log(title);
console.dir(title);
console.dir(document);
```

```javascript
title.innerHTML = "Hi! From JS";
title.style.color = '#34495e';

document.title = 'I own you now'
// 실제 바뀐 HTML 확인 가능
```

```javascript
function handleResize(){
    console.log(event);
    console.log("I have been resized")
}

window.addEventListener("resize", handleResize);
handleResize() 로 쓰면 자동으로 호출되고
resize 될 때 함수 호출하려면 handleResize 라고 써야함
```





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



자바스크립트는 이벤트에 반응하기 위해서 만들어졌다.

이벤트 : 웹사이트에서 발생하는 것들 click, resize, input, change, load, submit ..

이 이벤트를 중간에 가로챌 수 있다

window. 는 조금 다른 이벤트를 가지고 있다.

```javascript
function handleResize(){
    console.log("I have been resized")
}

window.addEventListener("resize", handleResize);
// handleResize() 로 쓰면 자동으로 호출되고
// resize 될 때 함수 호출하려면 handleResize 라고 써야함
```

```javascript
const title = document.getElementById("title");
// const title = document.querySelector("#title");

function handleClick() {
    title.style.color = 'black';
}

title.addEventListener("click", handleClick);
```



### if-else

조건

```javascript
if(condition) {
    block
} else {
    block
}
```

```javascript
if(10 > 5) {
    console.log("hi");
} else {
    console.log("ho");
}
```

if - else if - else if - ... - else



&& 둘 다 참이어야 참

|| or 적어도 하나가 참이면 참

true && true = true;

false && true = false;

true && false = false;

false && false = false;



true || true = true;

false || true = true;

true || false = true;

false || false = false;



```javascript
// prompt 는 안쓸꺼임
const age = prompt("How old are you");

console.log(age);

if(age >= 18 && age <= 21) {
    console.log('you can drink but you should not');
} else if(age > 21) {
    console.log("go ahead");
} else {
    console.log('you cant');
}
```

 

https://flatuicolors.com/ 

```javascript
// 누군가가 title 클릭할 때 console.log(title.style.color);
const title = document.querySelector("#title");

const BASE_COLOR = "#34495e";

function handleClick() {
    console.log(title.style.color);
}

function init() {
    title.style.color = BASE_COLOR;
    title.addEventListener("click", handleClick);
}

init();
```



```javascript
const title = document.querySelector("#title");

const BASE_COLOR = "rgb(52, 73, 94)";
const OTHER_COLOR = "#7f8c8d";

// 누군가 내 타이틀을 클릭하면
// 지금 가진 색깔 가져오기
function handleClick() {
    const currentColor = title.style.color;
    console.log(currentColor);
}

function init() {
    title.style.color = BASE_COLOR;
    title.addEventListener("click", handleClick);
}

init();
```

```javascript
const title = document.querySelector("#title");

const BASE_COLOR = "rgb(52, 73, 94)";
const OTHER_COLOR = "#7f8c8d";

function handleClick() {
    const currentColor = title.style.color;
    // 만약 현재의 색깔이 기본색과 같다면
    if(currentColor === BASE_COLOR) {
        // 누군가 처음 클릭하면 같을 것이므로
        // title.style.color 는 OTHER_COLOR가 될 것이다
        title.style.color = OTHER_COLOR;
    } else {
        title.style.color = BASE_COLOR;
    }
}

function init() {
    title.style.color = BASE_COLOR;
    title.addEventListener("click", handleClick);
}

init();
```



Javascript DOM event MDN 구글링

```javascript
function handleOffLine() {
    console.log("Bye Bye");
}

function handleOnLine() {
    console.log("Welcome back");
}

window.addEventListener("offline", handleOffLine);
window.addEventListener("online", handleOnLine);
```



HTML은 HTML 파일에서만 작업하고

CSS는 CSS 파일에서만 작업하게 하고

자바스크립트는 로직을 처리하게 하여서

자바스크립트가 웹사이트의 스타일을 처리하지 않게



index.html

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Something</title>
        <link rel="stylesheet" href="index.css"/>
    </head>

    <body>
        <h1 id="title" class="btn">This works!</h1>
        <script src="index.js"></script>
    </body>
</html>
```



index.css

```css
body {
    background-color: mintcream;
}

.btn {
    cursor : pointer;
}

h1 {
    color: #34495e;
    transition: color .5s ease-in-out;
}

.clicked {
    color: #7f8c8d;
}
```



index.js

```js
const title = document.querySelector("#title");

const CLICKED_CLASS = "clicked";

function handleClick() {
    // const hasClass = title.classList.contains(CLICKED_CLASS);
    // if(hasClass) {
    //     title.classList.remove(CLICKED_CLASS);
    // } else {
    //     title.classList.add(CLICKED_CLASS);
    // }
    title.classList.toggle(CLICKED_CLASS);
}

function init() {
    title.addEventListener("click", handleClick);
}

init();
```

