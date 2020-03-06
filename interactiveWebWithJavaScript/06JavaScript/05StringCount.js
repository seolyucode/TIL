// 주어진 단어(word)에 특정 알파벳(ch)이 몇 번 들어가는지 세어주는 함수
function countCharacter(word, ch) {
    var count = 0;
    word = word.toLowerCase();
    ch = ch.toLowerCase();

    // 코드를 작성해주세요.
    for(var i = 0; i < word.length; i++) {
        if(word[i] === ch) {
            count++;
        }
    }

    return count;
}
// function countCharacter(word, ch) {
//     var count = 0;

//     for (var i = 0; i < word.length; i++) {
//         if (word[i].toUpperCase() === ch.toUpperCase()) {
//             count++;
//         }
//     }
//     return count;
// }

// 단어 word에 알파벳 'A'가 몇 번 나오는지 세어주는 함수
function countA(word) {
    // 코드를 작성해주세요.
    var count = 0;
    word = word.toUpperCase();

    // 코드를 작성해주세요.
    for(var i = 0; i < word.length; i++) {
        if(word[i] === 'A') {
            count++;
        }
    }

    return count;
}
// function countA(word) {
//     var count = 0;

//     for (var i = 0; i < word.length; i++) {
//         if (word[i].toUpperCase() === 'A') {
//             count++;
//         }
//     }
//     return count;
// }

// 이미 countCharacter 함수를 만들었기에, 이 함수를 활용
// function countA(word) {
//     return countCharacter(word, 'A');
// }

// 테스트 코드
console.log(countCharacter('AbaCedEA', 'E'));
console.log(countCharacter('AbaCedEA', 'X'));
console.log(countA('AbaCedEA'));