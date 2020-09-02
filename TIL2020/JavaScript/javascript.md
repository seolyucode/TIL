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

```

