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



## Template Literal

ES6

ECMAScript 6

ES2015

ES7 ~ ES10

```javascript
function hello(name) {
  console.log(`Hello ${name}!`);
}

hello("velopert");
```

```javascript
function hello(name) {
  return `Hello ${name}!`;
  // return 쓰면 함수 종료
}

const result = hello("velopert");
console.log(result);
```

```javascript
function getGrade(score) {
  if (score === 100) {
    return "A+";
  } else if (score >= 90) {
    return "A";
  } else if (score === 89) {
    return "B+";
  } else if (score >= 80) {
    return "B";
  } else if (score === 79) {
    return "C+";
  } else if (score >= 70) {
    return "C";
  } else if (score === 69) {
    return "D+";
  } else if (score >= 60) {
    return "D";
  } else {
    return "F";
  }
}

const grade = getGrade(30);
console.log(grade);
```



## 화살표 함수

```javascript
const add = (a, b) => {
  return a + b;
}

const add1 = (a, b) => a + b;

const sum1 = add(1, 2);
console.log(sum1);

const hello = (name) => {
  console.log(`Hello, ${name}!`);
}

const sum = add(1, 2);
console.log(sum);

hello('Seolyu');
```



## 객체

```javascript
const dogName = "멍멍이";
const dogAge = 2;

console.log(dogName);
console.log(dogAge);

const dog = {
  name: "멍멍이",
  age: 2,
  "key with space": "asdf"
};

console.log(dog);
console.log(dog.name);
console.log(dog.age);

```

```javascript
const ironMan = {
  name: '토니 스타크',
  actor: '로버트 다우니 주니어',
  alias: '아이언맨',
};

const captainAmerica = {
  name: '스티븐 로저스',
  actor: '크리스 에반스',
  alias: '캡틴 아메리카'
};

console.log(ironMan);
console.log(captainAmerica);

function print(hero) {
  const text = `${hero.alias}(${hero.name}) 역할을 맡은 배우는 ${hero.actor} 입니다.`
  console.log(text);
}

print(ironMan);
print(captainAmerica);
```



## 객체 - 비구조화 할당

```javascript
const ironMan = {
  name: '토니 스타크',
  actor: '로버트 다우니 주니어',
  alias: '아이언맨',
};

const { name } = ironMan;
console.log(name);

const captainAmerica = {
  name: '스티븐 로저스',
  actor: '크리스 에반스',
  alias: '캡틴 아메리카'
};

console.log(ironMan);
console.log(captainAmerica);

function print(hero) {
  const { alias, name, actor } = hero;
  const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`
  console.log(text);
}

function print1({ alias, name, actor }) {
  const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`
  console.log(text);
}

print(ironMan);
print(captainAmerica);

print1(ironMan);
print1(captainAmerica);
```



## 객체 - 객체 안에 함수 넣기

```javascript
const dog = {
  name: '멍멍이',
  sound: '멍멍!',
  say: function say() {
    console.log(this.sound);
  },
  say1: function() {
    console.log(this.sound);
  },
  say2() {
    console.log(this.sound);
  },
  // 화살표 함수는 작동하지 않음
  say3: () => {
    console.log(this.sound);
  }
};

dog.say();
dog.say1();
dog.say2();
dog.say3();
```

```javascript
const dog = {
  name: "멍멍이",
  sound: "멍멍!",
  say: function say() {
    console.log(this.sound);
  },
  say1: function() {
    console.log(this.sound);
  },
  say2() {
    console.log(this.sound);
  },
  // 화살표 함수는 작동하지 않음
  say3: () => {
    console.log(this.sound);
  }
};

const cat = {
  name: '야옹이',
  sound: '야옹~'
}

cat.say = dog.say;
cat.say();

const catSay = cat.say;
catSay();

dog.say();
dog.say1();
dog.say2();
dog.say3();
```



## Getter Setter 함수

```javascript
const numbers = {
  a: 1,
  b: 2
};

numbers.a = 5;
console.log(numbers);
```

```javascript
const numbers = {
  a: 1,
  b: 2,
  get sum() {
    console.log('sum 함수가 실행됩니다!');
    return this.a + this.b;
  }
};

// numbers.a = 5;
// console.log(numbers);

console.log(numbers.sum);
numbers.b = 5;
console.log(numbers.sum);
```

```javascript
const dog = {
  _name: '멍멍이',
  get name() {
    console.log('_name을 조회합니다..');
    return this._name;
  },
  set name(value) {
    console.log('이름이 바뀝니다..' + value);
    this._name = value;
  }
};

console.log(dog._name);
console.log(dog.name);
dog.name = '뭉뭉이';
console.log(dog._name);
console.log(dog.name);
```

```javascript
const numbers = {
  _a: 1,
  _b: 2,
  sum: 3,
  calculate() {
    console.log('calculate');
    this.sum = this._a + this._b;
  },
  get a() {
    return this._a;
  },
  get b() {
    return this._b;
  },
  set a(value) {
    this._a = value;
    this.calculate();
  },
  set b(value) {
    this._b = value;
    this.calculate();
  }
};

console.log(numbers.sum);
numbers.a = 5;
numbers.b = 7;
numbers.a = 9;
console.log(numbers.sum);
console.log(numbers.sum);
```

```javascript
const numbers = {
  a: 1,
  b: 2,
  get sum() {
    console.log('sum');
    return this.a + this.b;
  }
};

console.log(numbers.sum);
numbers.a = 5;
numbers.b = 7;
numbers.a = 9;
console.log(numbers.sum);
console.log(numbers.sum);
console.log(numbers.sum);
console.log(numbers.sum);
```



## 배열

```javascript
const array = [1, 'blabla', {}, 4];
const objects = [
  { name: '멍멍이' },
  { name: '야옹이' }
];

console.log(array[0]);
console.log(objects[0]);
console.log(objects[1]);

objects.push({
  name: '멍뭉이'
})

console.log(objects);
console.log(objects.length);
```



## 반복문 - for

```javascript
for (let i = 0; i < 10; i++) {
  console.log(i);
}
```

```javascript
const names = ['멍멍이', '야옹이', '멍뭉이'];

for (let i = 0; i < names.length; i++) {
  console.log(names[i]);
}
```



## 반복문 - while

```javascript
let i = 0;
let isFun = false;

while (!isFun) {
  console.log(i);
  i++;
  if (i === 30) {
    isFun = true;
  }
}
```



## 반복문 - for...of, for...in

```javascript
const numbers = [10, 20, 30, 40, 50];

for (let number of numbers) {
  console.log(number);
}

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

const doggy = {
  name: '멍멍이',
  sound: '멍멍',
  age: 2
};

console.log(Object.entries(doggy));
console.log(Object.keys(doggy));
console.log(Object.values(doggy));
```

```javascript
const doggy = {
  name: '멍멍이',
  sound: '멍멍',
  age: 2
};

for (let key in doggy) {
  console.log(`${key}: ${doggy[key]}`);
}
```



## 반복문 - continue 와 break

```javascript
for (let i = 0; i < 10; i++) {
  // continue 는 그 다음 루프 돌게
  if (i === 2) continue;
  console.log(i);
  // break 는 반복문 끝냄
  if (i === 5) break;
}
```



## 반복문 - 연습과 퀴즈

```javascript
function sumOf(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}

const result = sumOf([1, 2, 3, 4, 5]);
console.log(result);
```



## 배열 내장함수 - forEach

```javascript
const superheroes = ["아이언맨", "캡틴 아메리카", "토르", "닥터 스트레인지"];

for (let i = 0; i < superheroes.length; i++) {
  console.log(superheroes[i]);
}
```

```javascript
const superheroes = ["아이언맨", "캡틴 아메리카", "토르", "닥터 스트레인지"];

function print(hero) {
  console.log(hero);
}

superheroes.forEach(print)
```

```javascript
const superheroes = ["아이언맨", "캡틴 아메리카", "토르", "닥터 스트레인지"];

superheroes.forEach(function(hero) {
  console.log(hero);
})
```

```javascript
const superheroes = ["아이언맨", "캡틴 아메리카", "토르", "닥터 스트레인지"];

superheroes.forEach(hero => {
  console.log(hero);
})
```



## 배열 내장함수 - map

```javascript
const array = [1, 2, 3, 4, 5, 6, 7, 8];

const squared = [];
for (let i = 0; i < array.length; i++) {
  squared.push(array[i] * array[i]);
}

console.log(squared);
```

```javascript
const array = [1, 2, 3, 4, 5, 6, 7, 8];

const squared = [];
array.forEach(n => {
  squared.push(n * n);
})

console.log(squared);
```

```javascript
const array = [1, 2, 3, 4, 5, 6, 7, 8];

const square = n => n * n;
const squared = array.map(square);

console.log(squared);
```

```javascript
const array = [1, 2, 3, 4, 5, 6, 7, 8];

const squared = array.map(n => n * n);

console.log(squared);
```

```javascript
const items = [
  {
    id: 1,
    text: 'hello'
  },
  {
    id: 2,
    text: 'bye'
  }
];

const texts = items.map(item => item.text);
console.log(texts);
```

```javascript
const superheroes = ['아이언맨', '캡틴 아메리카', '토르', '닥터 스트레인지'];
const index = superheroes.indexOf('토르');
console.log(index);
```

```javascript
const todos = [
  {
    id: 1,
    text: '자바스크립트 입문',
    done: true,
  },
  {
    id: 2,
    text: '함수 배우기',
    done: true,
  },
  {
    id: 3,
    text: '객체와 배열 배우기',
    done: true,
  },
  {
    id: 4,
    text: '배열 내장함수 배우기',
    done: false,
  }
]

const index = todos.findIndex(todo => todo.id === 3);
console.log(index);

const todo = todos.find(todo => todo.id === 3);
console.log(todo);

const todo1 = todos.find(todo => todo.done === false);
console.log(todo1);
```



## 배열 내장함수 - filter

```javascript
const todos = [
  {
    id: 1,
    text: '자바스크립트 입문',
    done: true,
  },
  {
    id: 2,
    text: '함수 배우기',
    done: true,
  },
  {
    id: 3,
    text: '객체와 배열 배우기',
    done: true,
  },
  {
    id: 4,
    text: '배열 내장함수 배우기',
    done: false,
  }
]

const tasksNotDone = todos.filter(todo => todo.done === false);
console.log(tasksNotDone);
```

```javascript
const tasksNotDone = todos.filter(todo => !todo.done);
console.log(tasksNotDone);
```



## 배열 내장함수 - splice 와 slice

```javascript
const numbers = [10, 20, 30, 40];
const index = numbers.indexOf(30);
console.log(index);
```

```javascript
const numbers = [10, 20, 30, 40];
const index = numbers.indexOf(30);
const spliced = numbers.splice(index, 1);
console.log(spliced);
console.log(numbers);
```

```javascript
const numbers = [10, 20, 30, 40];

const sliced = numbers.slice(0, 2);
console.log(sliced);
console.log(numbers);
```



## 배열 내장함수 - shift, pop, unshift, push

```javascript
const numbers = [10, 20, 30, 40];

// shift 첫번째 원소를 배열에서 추출
const value = numbers.shift();
numbers.shift();
numbers.shift();
console.log(value);
console.log(numbers);
```

```javascript
const numbers = [10, 20, 30, 40];

// pop 마지막 원소를 배열에서 추출
const value = numbers.pop();
numbers.pop();
console.log(value);
console.log(numbers);
```

```javascript
const numbers = [10, 20, 30, 40];

// shift 와 unshift
numbers.unshift(5);
const value1 = numbers.shift();
console.log(value1);
console.log(numbers);

// push 와 pop
numbers.push(50);
const value2 = numbers.pop();
console.log(value2);
console.log(numbers);
```

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const concated = arr1.concat(arr2);
console.log(concated);
```

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const concated = [...arr1, ...arr2];
console.log(concated);
```

```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// concat 은 기존 배열 수정 안하고
// 결과를 새로운 배열에 담는다
const concated = arr1.concat(arr2);
console.log(arr1);
console.log(arr2);
console.log(concated);
```

```javascript
const array = [1, 2, 3, 4, 5];
console.log(array.join());
console.log(array.join(' '));
console.log(array.join(', '));
```



## 배열 내장함수 - reduce

```javascript
const numbers = [1, 2, 3, 4, 5];

let sum = 0;
numbers.forEach(n => {
  sum += n;
});

console.log(sum);
```

```javascript
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum);
```

```javascript
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((accumulator, current, index, array) => {
  if (index === array.length - 1) {
    return (accumulator + current) / array.length;
  }
  return accumulator + current;
}, 0);
console.log(sum);
```



## 배열 내장함수 - reduce 다른 예시

```javascript
const alphabets = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'e'];
const counts = alphabets.reduce((acc, current) => {
  if (acc[current]) {
    acc[current] += 1;
  } else {
    acc[current] = 1;
  }
  return acc;
}, {})

console.log(counts);
```



