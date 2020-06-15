function printTriangle(height) {
    console.log('높이: ', height);
    var result = '';
    for(var i = 0; i < height; i++) {
        for(var j = 0; j < i+1; j++) {
            result += '*';
        }
        if (i===height-1) {
            break;
        }
        result += '\n';
    }
    console.log(result);
}

function printTriangle2(height) {
    text = '';
    for (var i = 0; i < height; i = i + 1) {
        text = text + '*';
        console.log(text);
    }
}

printTriangle(3);
printTriangle(5);