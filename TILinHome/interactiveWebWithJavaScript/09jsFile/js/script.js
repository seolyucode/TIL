$('#home').on('click', clickHome);
$('#seoul').on('click', clickSeoul);
$('#tokyo').on('click', clickTokyo);
$('#paris').on('click', clickParis);

$('#photo').on('mouseenter', mouseEnterPhoto);
$('#photo').on('mouseleave', mouseLeavePhoto);

$(document).on('keydown', processKeyEvent);

// 사진을 바꿔주는 함수
function clickHome() {
    // document.getElementById('photo').src = 'images/home.png';
    $('#photo').attr('src', 'images/home.png');

    // document.getElementById('home').style.fontWeight = 'bold';
    // document.getElementById('seoul').style.fontWeight = 'normal';
    // document.getElementById('tokyo').style.fontWeight = 'normal';
    // document.getElementById('paris').style.fontWeight = 'normal';
    $('#home').css('font-weight', 'bold');
    $('#seoul').css('font-weight', 'normal');
    $('#tokyo').css('font-weight', 'normal');
    $('#paris').css('font-weight', 'normal');
}

function clickSeoul() {
    // document.getElementById('photo').src = 'images/seoul.png';
    $('#photo').attr('src', 'images/seoul.png');

    // document.getElementById('seoul').style.fontWeight = 'bold';
    // document.getElementById('home').style.fontWeight = 'normal';
    // document.getElementById('tokyo').style.fontWeight = 'normal';
    // document.getElementById('paris').style.fontWeight = 'normal';
    $('#seoul').css('font-weight', 'bold');
    $('#home').css('font-weight', 'normal');
    $('#tokyo').css('font-weight', 'normal');
    $('#paris').css('font-weight', 'normal');
}

function clickTokyo() {
    // document.getElementById('photo').src = 'images/tokyo.png';
    $('#photo').attr('src', 'images/tokyo.png');

    // document.getElementById('tokyo').style.fontWeight = 'bold';
    // document.getElementById('home').style.fontWeight = 'normal';
    // document.getElementById('seoul').style.fontWeight = 'normal';
    // document.getElementById('paris').style.fontWeight = 'normal';
    $('#tokyo').css('font-weight', 'bold');
    $('#home').css('font-weight', 'normal');
    $('#seoul').css('font-weight', 'normal');
    $('#paris').css('font-weight', 'normal');
}

function clickParis() {
    // document.getElementById('photo').src = 'images/paris.png';
    $('#photo').attr('src', 'images/paris.png');

    // document.getElementById('paris').style.fontWeight = 'bold';
    // document.getElementById('home').style.fontWeight = 'normal';
    // document.getElementById('seoul').style.fontWeight = 'normal';
    // document.getElementById('tokyo').style.fontWeight = 'normal';
    $('#paris').css('font-weight', 'bold');
    $('#home').css('font-weight', 'normal');
    $('#seoul').css('font-weight', 'normal');
    $('#tokyo').css('font-weight', 'normal');
}


// 사진에 그림자
function mouseEnterPhoto() {
    $('#photo').css('box-shadow', '5px 10px');
}

function mouseLeavePhoto() {
    $('#photo').css('box-shadow', 'none');
}

// 키보드 이벤트 핸들링
function processKeyEvent(event) {
    // clickHome();
    // console.log(event);
    if (event['key'] === '1') {
        clickHome();
    } else if (event['key'] === '2') {
        clickSeoul();
    } else if (event['key'] === '3') {
        clickTokyo();
    } else if (event['key'] === '4') {
        clickParis();
    }
}