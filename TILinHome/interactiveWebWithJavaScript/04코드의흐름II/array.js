var arr = [2, 3, 5, 7];
arr.push(11);
console.log(arr);

function range(start, end, step) {
    var arr = [];
    
    if (start < end) {
        while(start < end) {
            arr.push(start);
            start += step;
        }
        return arr;
    } else if (start > end) {
        while(start > end) {
            arr.push(start);
            start += step;
        }
        return arr;
    } else {
        arr.push(start);
        return arr;
    }
}

function range2(start, end, step) {
    var arr = [];
    var idx = 0;

    if (start < end) {
        for (var i = start; i < end; i += step) {
            arr[idx] = i;
            idx++;
        }
    } else {
        for (var i = start; i > end; i += step) {
            arr[idx] = i;
            idx++;
        }
    }
    return arr;
}

// 결과 예시
console.log(range(1, 6, 1));
console.log(range(3, 10, 2));
console.log(range(10, -10, -4));

console.log(range2(1, 6, 1));
console.log(range2(3, 10, 2));
console.log(range2(10, -10, -4));