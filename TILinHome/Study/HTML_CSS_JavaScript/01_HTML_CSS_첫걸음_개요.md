heropy.blog



### HTML(Hyper Text Markup Language)

페이지에 제목, 문단, 표, 이미지, 동영상 등 정의

그 구조와 의미를 부여하는 정적 언어로 웹의 구조를 담당

구조(Semantic) 만드는 것에 집중 

### CSS(Cascading Style Sheets)

마크업 언어(HTML, XML 등)가 실제 표시되는 방법(색상, 크기, 폰트, 레이아웃 등)을 지정

콘텐츠 구조를 꾸며주는 정적 언어로 웹의 시각적 표현 담당

예쁘게 만들기(적당한 크기, 아름다운 색상, 원하는 위치 지정) 

### JavaScript

콘텐츠를 바꾸고 움직이는 등 페이지를 동적으로 꾸며주는 역할을 하는 프로그래밍 언어

웹의 동적 처리 담당



웹 표준(Web Standard) '웹에서 사용되는 표준 기술이나 규칙'

W3C의 권고안에서 나온 기술

표준화 제정 단계의 '권고안(REC)'에 해당하는 기술



크로싱 브라우징(Cross Browsing)

각각의 브라우저에서 동일한 결과물이 나오도록

동일한 사용자 경험(같은 화면, 같은 동작 등)을 줄 수 있도록 제작하는 기술, 방법 등



웹 접근성

정상적인 웹 콘텐츠 사용이 가능한 일반 사용자부터 고령자, 장애인 같은 신체적, 환경적 조건에 제한이 있는 사용자를 포함해 모든 사용자들이 동등하게 접근할 수 있는 웹 콘텐츠를 제작하는 방법

영상에 자막 넣기, 키보드 통해서도 웹 이용할 수 있게, 이미지에 대체 텍스트 제공 등

cf) 웹 콘텐츠 접근성 지침 참고



HTML, CSS, JS 를 위한 웹 개발(프론트엔드, Node.js) 에디터 중 실무에서 많이 사용되는 크로스 플랫폼(Windows, macOS) 에디터

* Sublime Text
* Atom
* Brackets
* VS Code
* WebStorm



VS Code

확장기능

* Korean Language Pack for Visual Studio Code
* Beautify
  * 파일 - 기본설정 - 바로 가기 키
  * 기여 - Beautify selection(설명) 이름 복사
  * 바로 가기 키에서 검색 후 설정(Ctrl + Alt + L)
* Live Server - Go Live



바로 가기 키에서 검색할 때

"ctrl+alt 이런식으로 " 사용해서 검색할 수 있음

Ctrl + F -> Ctrl + H 찾기/바꾸기

Ctrl + \ 화면 분할



코드 드래그 후 Ctrl + Shift + P

wrap 검색

Emmet:약어로 래핑

div



웹에서 사용하는 이미지

비트맵과 벡터 이미지

### 비트맵(Bitmap) : 

각 픽셀이 모여 만들어진 정보의 집합. 레스터(Raster) 이미지

픽셀 단위로 화면에 렌더링

jpg(JPEG), png, gif, webp

### 벡터(Vector) : 

수학적 정보의 형태(Shape)들이 만들어내는 결과물

이미지가 가지고 있는 점, 선, 면의 위치(좌표), 색상 등의 정보를 온전히 가지고 있으며 그를 화면에 렌더링

해상도로부터 자유롭게 렌더링

이미지 확대/축소에 따른 용량 변화가 없음

SVG



특수 문자 용어 정리

` Grave(그레이브)

~ Tilde(틸드) 물결표시

! Exclamation(익스클러메이션) mark 느낌표

@ At(엣) sign 골뱅이

#### # Number(넘버) sign, Sharp(샵) 샵, 우물 정

$ Dollar(달러) sign 달러

% Percent(퍼센트) sign 퍼센트

^ Caret(캐럿)

& Ampersand(엠퍼센드)

#### * Asterisk(에스터리스크) 별표

#### - Hyphen(하이픈), Dash(대쉬) 마이너스

_ Underscore(언더스코어), Low dash(로대쉬) 밑줄

= Equals(이퀄) sign 이꼬르

" Quotation(쿼테이션) mark 큰 따옴표

' Apostrophe(아포스트로피) 작은 따옴표

: Colon(콜론) 땡땡이

; Semicolon(세미콜론) 털 달린 땡땡이

, Comma(콤마) 쉼표

. Period(피리어드), Dot(닷) 점, 마침표

? Question(퀘스천) mark 물음표

/ Slash(슬래쉬)

| Vertical bar(버티컬 바)

\ Backslash(백슬래쉬)

() Parenthesis(퍼렌서시스) (소)괄호

{} Brace(브레이스) 중괄호

[] Bracket(브래킷) 대괄호

<> Angle Bracket(앵글 브래킷) 꺽쇠괄호



오픈소스와 라이센스

오픈소스: 어떤 제품을 개발하는 과정에 필요한 소스 코드나 설계도를 누구나 접근해서 열람할 수 있도록 공개하는 것

#### Apache License: 

아파치 소프트웨어 재단에서 자체 소프트웨어에 적용하기 위해 만든 라이선스

개인적/상업적 이용, 배포, 수정, 특허 신청 가능

#### MIT License: 

매사추세츠공과대학(MIT)에서 소프트웨어 학생들을 위해 개발한 라이선스

개인 소스에 이 라이선스를 사용하고 있다는 표시 지켜주면 되며, 나머지 사용에 대한 제약 없음

#### BSD License: 

BSD(Berkeley Software Distribution)는 버클리 캘리포니아대학에서 개발한 라이선스

라이선스 표시만 지켜주면 됨

#### Beerware:

오픈소스 개발자에게 맥주를 사줘야 하는 라이선스



OpenSource.org



