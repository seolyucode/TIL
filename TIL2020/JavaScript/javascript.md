learnjs.vlpt.us

http://codesandbox.io/



```javascript
let a = 1;
console.log(a--);  // 1
console.log(a);  // 0
```



```
// 우선순위대로
// NOT !
// AND &&
// OR ||

const a = !false;
console.log(a);  // true

const a = true && true;
console.log(a);  // true 양쪽값 모두 true 일 때만 true

const a = true || true;
console.log(a);  // 둘 중 하나라도 true면 true

const value = !(true && false || true && false || !false);
// !(true && false || true && false || true)
// !(false || false || true)
// !(true)
// false

const a = 1;
const b = 1;
const equals = a === b;  // 두 값 비교 ===
console.log(equals);  // true

== 와 ===
==는 타입을 비교하지 않음 0이랑 false 같다고 함. null undefined도 같다고 함

const a = 'a';
const b = 'b';
const notEquals = a !== b;
console.log(notEquals);  // true

```



```javascript
const device = 'iphone';

switch (device) {
    case 'iphone':
        console.log('아이폰');
        break;
    case 'ipad':
        console.log('아이패드');
        break;
    case 'galaxy note':
        console.log('갤노트');
        break;
    default:
        console.log('모름');        
}
```



파라미터 -> 함수 -> 결과

```javascript
function add(a, b) {
    return a + b;
}

const sum = add(1, 2);
console.log(sum);  // 3
```

```javascript
function hello(name) {
    console.log('Hello, ' + name + '!');
}

hello('seolyu');  // Hello, seolyu!
```

```javascript
function hello(name) {
    console.log(`Hello ${name}!`);
}

hello('seolyu');
```

```javascript
function hello(name) {
    return `Hello ${name}!`;
}

const result = hello('seolyu');
console.log(result);
```



```javascript
function getGrade(score) {
    if (score === 100) {
    	return 'A+';
    } else if (score >= 90) {
        return 'A';
    } else if (score === 89) {
        return 'B+';
    } else if (score >= 80) {
        return 'B';
    } else if (score === 79) {
        return 'C+';
    } else if (score >= 70) {
        return 'C';
    } else if (score === 69) {
        return 'D+';
    } else if (score >= 60) {
        return 'D';
    } else {
        return 'F';
    }
}

const grade = getGrade(100);
console.log(grade);
```



```javascript
const add = (a, b) => a + b;

const sum = add(1, 2);
console.log(sum);  // 3


const hello = (name) => {
    console.log(`Hello, ${name}!`);
}

hello('seolyu');  // Hello, seolyu
```



객체

```javascript
const dogName = '멍멍이';
const dogAge = 2;

console.log(dogName);
console.log(dogAge);
```

```javascript
const dog = {
    name: '멍멍이',
    age: 2,
    'key with space': 'asdf',
}

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

const { name } = ironMan;
console.log(name);

const captainAmerica = {
    name: '스티븐 로저스',
    actor: '크리스 에반스',
    alias: '캡틴 아메리카'
}

console.log(ironMan);
console.log(captainAmerica);

function print(hero) {
    const text = `${hero.alias}(${hero.name}) 역할을 맡은 배우는 ${hero.actor} 입니다.`;
    console.log(text);
}

print(ironMan);
print(captainAmerica);
```

비구조화 할당

```javascript
function print(hero) {
    const { alias, name, actor } = hero;
    const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`;
    console.log(text);
}
```

```javascript
function print({ alias, name, actor }) {
    const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`;
    console.log(text);
}
```



객체 안에 함수 넣기

```javascript
const dog = {
    name: '멍멍이',
    sound: '멍멍!',
    say: function say() {
        console.log(this.sound);
    }
};
```

