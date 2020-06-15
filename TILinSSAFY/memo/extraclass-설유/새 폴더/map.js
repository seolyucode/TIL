Array.prototype.myMap = function (fn) {
    const originArray = this;
    const returnArray = [];

    for (const e of originArray) {
        returnArray.push(fn(e));
    }
    return returnArray;
}

const double = function (num) {
    return num * 2;
}

[1,2,3].myMap(double);