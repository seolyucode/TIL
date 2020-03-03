function getSecondBiggestNumber(arr) {
    // 코드를 작성하세요.
    var first = 0;
    for(var i = 0; i < arr.length; i++) {
        if (arr[i] > first) {
            first = arr[i];
        }
        if (i == arr.length-1) {
            for(var j = 0; j < arr.length; j++) {
                if (first === arr[j]) {
                    arr[j] = 0;
                }
            }
        }
    }
    var second = 0;
    for(var k = 0; k < arr.length; k++) {
        if (arr[k] > second) {
            second = arr[k];
        }
    }
    return second;
}

function getSecondBiggestNumber2(arr) {
    var first = arr[0];
    var second = arr[1];
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        } else if (arr[i] > second) {
            second = arr[i];
        }
    }
    return second;
}

// 테스트 코드
console.log(getSecondBiggestNumber([4, 7, 2, 1, 9, 3, 6, 5]));
console.log(getSecondBiggestNumber([80, 2, 44, 21, 92, 3, 51]));
console.log(getSecondBiggestNumber([4, 7, 6, 5]));