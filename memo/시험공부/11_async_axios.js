// axios 는 XHR(XMLHttpRequest)를 보내주고 그 결과를 promise 객체로 반환해주는 라이브러리이다.

// 파이썬(blocking)
// 자바스크립트(non-blocking)

/*
axios 는 promise 객체를 반환하여 .then 을 통해 해당하는 작업이 (axios 요청작업)
완료된(resolve) 경우 실행 될 로직을 구현할 수 있다.
(.catch 에서는 reject 된 결과를 받아서 처리할 수 있다.) - 콜백 지옥 해결 위한 약속

* 브라우저는 싱글쓰레드에서 이벤트 기반(event driven) 방식으로 실행됨
* call stack : 함수가 호출되면 순차적으로 call stack에 쌓이고 순차적으로 실행
               task가 종료하기 전까지는 다른 task를 수행할 수 없다.
* callback queue : 비동기처리 함수의 콜백, 타이머(setTimeout), 이벤트헨들러 등이
                   기록되는 곳으로 이벤트 루프에 의해 특정시점에 콜 스택으로 이동되어 실행 됨
* event loop : 콜 스택과 콜백 큐에 작업이 (실행될 함수) 있는지 확인하며 작업을 실행
*/
