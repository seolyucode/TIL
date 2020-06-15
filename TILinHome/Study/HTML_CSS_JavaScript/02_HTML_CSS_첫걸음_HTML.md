#### HTML

```html
<태그>CONTENT</태그>
```

전체를 요소(element)라고 함

각각은 tag

태그, 요소 거의 같게 씀



속성(Attributes) 과 값(Value)

태그(요소)의 기능을 확장하기 위해 '속성' 사용 가능

```html
<TAG 속성="값"></TAG>
```

```html
<img src="./my_photo.jpg" alt="내 프로필 사진" />

위 코드에서 src 는 source 
이미지로 삽입할 리소스는 어디에 있는지 src 의 값으로 경로를 입력

띄어쓰기로 구분

alt 는 alternative 대체 텍스트
이미지가 삽입되지 못했을 때 나올 글자

빈 태그(Empty tag) : 닫히는 태그가 없음
```

```html
<이미지삽입 소스위치="./my_photo.jpg" 대체텍스트="내 프로필 사진" />
```

```html
<div class="name">홍길동</div>

div 는 division 분할
div 는 의미를 가지고 있지 않음
class 속성 사용해서 태그 별명
```

```html
<의미없는분할 태그별명="name">홍길동</의미없는분할>
```



부모와 자식 요소

태그A가 태그B의 콘텐츠로 사용되면,

태그B는 태그A의 부모 요소, 태그A는 태그B의 자식 요소

```html
<PARENT>
	<CHILD></CHILD>
</PARENT>
```

```html
<section class="fruits">
	<h1>과일 목록</h1>
    <ul>
        <li>사과</li>
        <li>딸기</li>
        <li>바나나</li>
        <li>오렌지</li>
    </ul>
</section>
```

section 입장에서 li 태그는 후손(자손, 하위) 요소

부모 이상은 조상(상위) 요소



빈 태그(Empty tag)

```html
<!-- '/' 가 없는 빈 태그 -->
<TAG>

<!-- '/' 가 있는 빈 태그 -->
<TAG/>
<TAG />
```

HTML5 에서는 위 2가지 형태 모두 사용 가능

XHTML 버전이나 린트(Lint) 환경 혹은 프레임워크 세팅에 따라 / 를 사용하는 것이 필수가 될 수 있음

빈태그에 보통 속성="값" 붙음



DOCTYPE(DTD, 버전 지정)

Document Type Definition 은 마크업 언어에서 문서 형식을 정의

이는 웹 브라우저에 우리가 제공할 HTML 문서를 어떤 HTML 버전의 해석 방식으로 구조화하면 되는지 알려준다

(HTML 은 크게 1, 2, 3, 4, X- 5 버전이 있다)

현재의 표준 모드는 HTML5

HTML 문서의 범위를 나타내는(의미하는) 태그들

```html
<!DOCTYPE html>
<html>
    <head>
        문서의 정보
    </head>
    <body>
        문서의 구조
    </body>
</html>
```



HEAD 태그(TITLE, META, LINK, STYLE, SCRIPT)

#### TITLE(웹 페이지의 제목) : 

HTML 문서의 제목 정의

웹 브라우저의 각 사이트 탭에서 이름으로 표시

```html
<head>
    <title>네이버</title>
</head>
```

META(웹 페이지의 정보):

HTML 문서(웹페이지)에 관한 정보(표시 방식, 제작자(소유자), 내용, 키워드 등)를 검색엔진이나 브라우저에 제공

빈(Empty) 태그

```html
<head>
    <meta charset="UTF-8">
    <meta name="author" content="홍길동">
    <meta name="description" content="우리 사이트가 최고!">
</head>
```

```html
<문서의정보범위>
    <정보 문자인코딩방식="UTF-8">
    <정보 정보종류="사이트제작자" 정보값="홍길동">
    <정보 정보종류="사이트설명" 정보값="우리 사이트가 최고!">
</문서의정보범위>
```

LINK(CSS 불러오기)

외부 문서를 연결할 때 사용

특히 HTML 외부에서 작성된 CSS 문서(xxx.css 파일)를 불러와 연결할 때 사용

빈(Empty) 태그

```html
<head>
    <link rel="stylesheet" href="./css/main.css">
    <link rel="icon" href="./favicon.png">
</head>

<문서의정보범위>
	<외부문서연결 관계="CSS" 문서경로="./css/main.css">
    <외부문서연결 관계="사이트대표아이콘" 문서경로="./favicon.png">    
</문서의정보범위>
```

STYLE(CSS 작성하기)

CSS 를 외부 문서에서 작성하여 연결하는 것이 아니고 HTML 문서 내부에 작성할 때 사용

```css
<style>
    img {
        width: 100px;
        height: 200px;
    }
    p {
        font-size: 20px;
        font-weight: bold;
    }
</style>

<!-- 다음과 같이 이해할 수 있습니다. -->
<스타일정의>
	<!-- CSS 코드 -->
</스타일정의>
```

SCRIPT(JS 불러오거나 작성하기)

HTML 문서에서 CSS는, 작성된 CSS를 <link> 로 불러오거나 <style></style> 안에 작성할 수 있다.

JS는 <script></script> 로 이 2가지 방식을 모두 사용할 수 있다

```html
<!-- 불러오기 -->
<script src="./js/main.js"></script>

<!-- 작성하기 -->
<script>
	function windowOnClickHandler(event) {
        console.log(event);
    }
    window.addEventListener('click', windowOnClickHandler);
</script>


<!-- 다음과 같이 이해할 수 있다 -->

<!-- 불러오기 -->
<자바스크립트 문서경로="./js/main.js"></자바스크립트>
```



HTML 문서의 구조

<body></body> 안에서 사용하는 태그들은 HTML 문서의 구조를 나타냄

DIV(막 쓰는 태그)

문서의 부분이나 섹션을 정의. 명확한 의미를 가지지 않기 때문에 정말 많은 경우 단순히 특정 범위를 묶는(wrap) 용도로 사용

보통 이렇게 묶인 부분들에 CSS나 JS를 적용



IMG(이미지 넣는 태그)

<img> 는 HTML 에 이미지를 삽입할 때 사용

(웹 페이지에 이미지를 삽입하는 방식은 크게 2가지로, 'HTML에서 삽입(IMG)' 과 'CSS에서 삽입(background)'이 있다)

```html
<body>
    <img src="./kitty.png" alt="냥이">
</body>

<body>
    <이미지 경로="./kitty.png" 대체텍스트="냥이">
</body>
```

속성 중 src 는 (필수)이미지의 URL

alt 는 (필수)이미지의 대체 텍스트(alternate)를 지정

속성이 누락되면 웹 표준에 어긋남



W3C validator 에 접속하여 작성한 HTML 문서를 업로드하고 테스트를 시작



 https://heropcode.github.io/GitHub-Responsive/ 

