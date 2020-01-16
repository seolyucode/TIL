$(document).ready(function() {
    'use strict';

    paper.install(window);
    paper.setup(document.getElementById('mainCanvas'));

    // TODO
    // var c = Shape.Circle(200, 200, 50);
    // c.fillColor = 'green';
    
    /*
    var c;
    for(var x=25; x<400; x+=50) {
        for(var y=25; y<400; y+=50) {
            c = Shape.Circle(x, y, 20);
            c.fillColor = 'green';
        }
    }
    */   

    var c = Shape.Circle(200, 200, 80);
    c.fillColor = 'black';
    
    var text = new PointText(200, 200);
    text.justification = 'center';
    text.fillColor = 'white';
    text.fontSize = 20;
    text.content = 'hello world';
   
    var tool = new Tool();  // tool 객체 생성. 객체를 만들면 거기에 이벤트 핸들러를 연결 가능

    // onMouseDown 이벤트 핸들러를 연결. 사용자가 마우스를 클릭할 때마다 이 핸들러에 연결한 함수가 호출
    // 사용자가 캔버스 어딘가를 마우스로 클릭해야만 function 다음에 있는 중괄호 사이의 코드가 실행
    tool.onMouseDown = function(event) {

        var c = Shape.Circle(event.point, 20);
        c.fillColor = 'green';
    }

    paper.view.draw();

    console.log('main.js loaded');
});