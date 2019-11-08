const me = {  // Object - 객체
    name: '이설유',  // key가 한단어일 때는 따옴표 생략 가능
    'phone number' : '01012345678',  // key가 여러 단어일 때는 써야함
    electronicDevice: {
        phone: 'iphone Xs',
        tablet: 'ipad pro3',
        laptop: 'macbook pro',
    },
};

// KEY - VALUE json
// JavaScript Object Notation : JS 의 Object 처럼 표기하는 방법

me.electronicDevice.phone
me['electronicDevice']['phone']