### 개발자 실력 향상을 위한 공부법

1. 우리는 모든 것을 다 알지 못한다.
2. 문제 해결능력 연습이 중요하다.
3. 능동적으로 강의를 들어야 한다.
4. 이해를 먼저 하고, 노트를 정리
5. 원활한 의사소통 정말 중요하다.

---

### WEB APIs

브라우저에 대해 완벽히 이해

APIs : Application Programming Interfaces

---

DOM(Document Object Model) APIs

Network APIs

Graphics APIs

Audio/Video APIs

Device APIs

File APIs

Storage APIs

https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction

https://developer.mozilla.org/en-US/docs/Web/API

https://www.thoughtco.com/what-javascript-cannot-do-2037666

---

HTTP <- Hypertext Transfer Protocol

서버가 어떻게 통신하는지 통신규약을 정해 놓은 것

클라이언트가 서버에게 정보를 요청하고 다시 서버에서 정보를 받아오는 request를 하고 response를 받아오는 방식으로 이루어져 있음

HTTPS는 HTTP에 S가 더해진 것 Hypertext Transfer Protocol Secure

즉 정보를 주고받는 것들이 잘 감싸져있는 보안 처리가 잘 된. secure하게 encrypt가 되어서

몇몇 Web APIs는 HTTPS 환경에서만 동작 가능

External APIs를 활용해 웹 어플리케이션 제작

---

브라우저에서 웹 페이지를 열면 Window(전체적인 창)라는 전체적인 오브젝트가 존재, 

Window 안에 페이지가 표기되는 부분이 Document 오브젝트(HTML에서 작성한 요소들이 표기),

Navigator(사용자 눈에는 보이지 않지만 전체적으로 Window에 관련된 즉 브라우저 자체 관련 정보들이 담겨있음) 오브젝트

window -> DOM, BOM(Browser Object Model - navigator, location, fetch, storage ... ), JavaScript ..

`console.log(window)`

`console.log(this)`

Window는 글로벌 오브젝트

size, scroll, load 확인 때 많이 쓰임

---

### Window Size

```
window.screen <- 모니터 사이즈
------------------------------------
아래는 브라우저 사이즈 변경되면 업데이트
window.outer <- 브라우저 사이즈
window.inner <- 페이지가 표기되는 부분 전체
documentElement.clientWidth <- 스크롤바 제외한 순수 document문서 자체
```

---

### coordinates (좌표)

왼쪽 최상위가 (0, 0)

`Element.getBoundingClientRect()`  <- 요소가 브라우저 위에서 즉 window 위에서 얼마나 멀리 떨어져 있는지, 크기 얼마인지 등

left <- x축

top <- y축

bottom <- 브라우저 제일 위에서 요소 밑까지. 

right <- 왼쪽에서 제일 끝까지

cf) CSS 에서는 포지션을 absolute나 relative로 지정하게 되면 top과 left / right(브라우저 제일 오른쪽으로부터 떨어진 거리)과 bottom(브라우저 제일 밑에서 떨어진 거리) 이용. 



### Client x,y  vs  Page x,y

Client x, y  <- 브라우저 window에서 좌표값에 해당

Page x, y  <- 문서의 제일 시작점부터 x, y 계산

---

### Window load



---

