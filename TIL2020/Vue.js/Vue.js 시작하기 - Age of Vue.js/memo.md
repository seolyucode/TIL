chrome

visual studio code

node.js

vue.js dev tools

---

joshua1988/learn-vue-js

https://github.com/joshua1988/learn-vue-js

---

- Vetur
- Night Owl
- Material Icon Theme
- Live Server
- ESLint
- Prettier
- Auto Close Tag
- Atom Keymap

---

Vue는 MVVM 패턴의 뷰모델(ViewModel) 레이어에 해당하는 화면(View)단 라이브러리

![image-20200908213931410](./imgs/image-20200908213931410.png)

---

Ctrl + \ 패널 토글 단축키

---

뷰 인스턴스

뷰로 개발할 때 필수로 생성해야 하는 코드

```vue
new Vue();
```

---

뷰 컴포넌트

화면의 영역을 구분하여 개발할 수 있는 뷰의 기능

재사용성이 올라가고 빠르게 화면 제작

---

상위에서 하위로 데이터 내려줌, 프롭스 속성

하위에서 상위로 이벤트 올려줌, 이벤트 발생

---

뷰 라우터

뷰 라이브러리를 이용하여 싱글 페이지 애플리케이션을 구현할 때 사용하는 라이브러리

---

액시오스

뷰에서 권고하는 HTTP 통신 라이브러리

Promise 기반의 HTTP 통신 라이브러리이며 상대적으로 다른 HTTP 통신 라이브러리들에 비해 문서화가 잘되어 있고 API가 다양

cf) Ajax(Asynchronous JavaScript and XML, 에이잭스) 



자바스크립트의 비동기 처리 패턴

1. callback
2. promise
3. promise + generator
4. async & await

https://github.com/axios/axios

https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/

https://joshua1988.github.io/web-development/javascript/promise-for-beginners/

https://joshua1988.github.io/web-development/javascript/js-async-await/

---

https://jsonplaceholder.typicode.com/

https://joshua1988.github.io/web-development/translation/javascript/how-js-works-inside-engine/

https://joshua1988.github.io/web-development/http-part1/

https://developers.google.com/web/tools/chrome-devtools/

---

뷰의 템플릿 문법

뷰로 화면을 조작하는 방법

템플릿 문법은 크게 데이터 바인딩과 디렉티브로 나뉜다

* 데이터 바인딩

  뷰 인스턴스에서 정의한 속성들을 화면에 표시하는 방법

  가장 기본적인 데이터 바인딩 방식은 콧수염 괄호(Mustache Tag)

* 디렉티브

  뷰로 화면의 요소를 더 쉽게 조작하기 위한 문법

  화면 조작에서 자주 사용되는 방식들을 모아 디렉티브 형태로 제공

https://vuejs.org/v2/guide/forms.html#ad

---

https://vuejs.org/v2/guide/computed.html#ad

---

Vue CLI

`node -v`

`npm -v`

`npm install -g @vue/cli`  // 권한 없으면 앞에 sudo

https://stackoverflow.com/questions/5926672/where-does-npm-install-packages

[Vue CLI 2.x]

vue init '프로젝트 템플릿 유형' '프로젝트 폴더 위치'

vue init webpack-simple '프로젝트 폴더 위치'



[Vue CLI 3.x]

vue create '프로젝트 폴더 위치'

`vue create vue-cli`

`cd vue-cli`

`npm run serve`

---

- Reactivity
- 인스턴스
- 컴포넌트
- 컴포넌트 통신
  * props
  * event emit
- HTTP 통신 라이브러리 (axios)
- 템플릿 문법
  * 데이터 바인딩
  * 뷰 디렉티브
- Vue CLI
- 싱글 파일 컴포넌트