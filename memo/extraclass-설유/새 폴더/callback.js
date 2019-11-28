// 주객 전도
// 1. 함수를 정의한다.
const adder = function (x, y) {
    return x + y
};
// 2. 함수를 호출한다.
adder(1, 2)

const numbersAddEach = function (numbers) {
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

const numbersSubEach = function (numbers) {
    let sum = 0;
    for (const number of numbers) {
        sum -= number;
    }
    return sum;
};

const numbersMulEach = function (numbers) {
    let sum = 1;
    for (const number of numbers) {
        sum *= number;
    }
    return sum;
};

const numbersDivEach = function (numbers) {
    let sum = 1;
    for (const number of numbers) {
        sum /= number;
    }
    return sum;
};

// 배열의 숫자들을 각각 [동사 === 함수]?? 하는 함수: (??는 니가 써와라) :
// callback 은 다른 이름으로 써도 됨
const numbersEach = function (numbers, callback) {
    let acc=0;
            //   1       [1,2,3]   
            //   2
            //   3
    for (const number of numbers) {
        // acc = doSomething(number, acc);
        // 1          add(1     , 0)
        // 3          add(2     , 1)
        // 6          add(3,    , 3)
        acc = callback(number, acc);
    }
    return acc;
};

// 뺀다
const sub = function (number, acc) {
    return acc - number;
};

numbersEach([1,2,3], function (acc=0, number) {
    return acc + number;
});

numbersEach([1,2,3], sub);