웹 개발의 변화

Ajax -> SPA(MVC) -> Web component



* 일반 웹 애플리케이션 : 서버로부터 새로운 페이지를 받아 전체 리소스를 로드하고 처음부터 렌더링 한다
* 단일 페이지 웹 애플리케이션 : Ajax요청을 통해 변경되는 부분에 필요한 데이터만 받아와 해당 부분만 렌더링을 한다



AngularJS : 구글이 만든 단일 페이지 웹 애플리케이션 개발을 위한 자바스크립트 프레임워크



Web Component <- 커스텀 엘리먼츠 + 쉐도우 돔 + HTML Import + HTML 템플릿



Angular : 구글이 만든 웸 애플리케이션 플랫폼으로서 다양한 플랫폼에서 동작할 수 있게 하는 개발 툴과 기능들을 제공



Framework 에서 Platform 으로



AngularCLI는 node.js 프로젝트라서

node.js 설치되어있어야함(LTS)



`node --version`

`npm install -g @angular/cli`

`ng --version`

`ng new first-app`



`cd first-app`

`tree -L 1`  ?

`tree src`  ?



`ng serve`

주소 복붙



`ng --help`  ?



...



Module : 세부 구현이 숨겨지고 공개 API를 이용해 다른 코드에서 재사용 가능한 코드



ES6 Module : + 변수의 스콥이 모듈로 제한