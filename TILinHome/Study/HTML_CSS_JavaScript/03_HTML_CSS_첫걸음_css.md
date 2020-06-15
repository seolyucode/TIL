CSS 문법은 HTML 보다 더 쉽다.

선택자, 속성, 값이 있으며 무엇을 의미하는지 이해

```css
div {
    font-size: 20px;
    color: red;
}

/* 다음과 같이 이해할 수 있다. */
선택자 {
    속성: 값;
    속성: 값;
}
```

선택자(selector)는 HTML에 스타일(CSS)을 적용하기 위해 HTML의 특정한 요소를 선택하는 사인(sign).

```html
<div>
    <h1>제목..</h1>
    <p>본문..</p>
</div>
```

```css
h1 {
    color: red;
}
p {
    color: blue;
}
```



속성(Properties)과 값(Value)

css 속성은 Properties 

HTML 속성은 attribute

속성과 값은 글자색은 무엇, 너비는 얼마, 여백은 얼마 같은 스타일을 지정할 때 사용

```css
div {
    color: red;  /* 글자색은 빨강 */
    font-size: 20px;  /* 글자 크기는 20px */
    width: 300px;  /* 가로 너비는 300px */
    margin: 20px;  /* 바깥 여백은 20px */
    padding: 10px 20px;  /* 안쪽 여백은 위아래 10px, 좌우 20px */
    position: absolute;  /* 위치는 부모 요소 기준 */
}
```

선택자 종류

속성: 값;



태그에 직접 작성하기(인라인) - 선언 방식

HTML 태그에 직접 작성하기 때문에 선택자 필요 없음

```html
<div style="color: red;">태그에 직접 작성1</div>  <!-- red -->
<div style="color: red;">태그에 직접 작성2</div>  <!-- red -->
<div style="color: red;">태그에 직접 작성3</div>  <!-- red -->
<div style="color: red;">태그에 직접 작성4</div>  <!-- red -->
```



HTML 에 포함하기(내장) embeded

CSS 만 따로 작성하기 때문에 선택자가 필요

CSS 코드가 HTML 의 <style></style> 안에 포함되어 있음

```html
<head>
    <style>
        div {
            color: red;
        }    
    </style>
</head>
<body>
    <div>HTML에 포함1</div>  <!-- red -->
    <div>HTML에 포함2</div>  <!-- red -->
    <div>HTML에 포함3</div>  <!-- red -->
</body>
```

style 태그는 css 정보



HTML 외부에서 불러오기

```html
<!-- HTML 1 -->
<head>
    <link rel="stylesheet" href="/css/main.css">
</head>
<body>
    <div>HTML에 외부에서 불러오기1</div>  <!-- red -->
</body>
```

```html
<!-- HTML 2 -->
<head>
    <link rel="stylesheet" href="/css/main.css">
</head>
<body>
    <div>HTML에 외부에서 불러오기2</div>  <!-- red -->
</body>
```

```css
/* main.css */
div {
    color: red;
}
```



선택자(HTML의 특정한 요소를 선택하는 사인(sign))

태그로 찾기

선택자를 입력하는 부분에 적용하려는(찾으려는) 태그의 이름을 입력

```css
/* <h1>은 글자색이 빨강이야! */
h1 {
    color: red;
}
/* <p>는 글자색이 파랑이야! */
p {
    color: blue;
}
```



클래스로 찾기

좀 더 명확하게 원하는 요소를 찾기 위해서 '클래스 선택자' 존재

```css
/* class="title" 은 글자색이 빨강이야! */
.title {
    color: red;
}
/* class="main-text" 는 글자색이 파랑이야! */
.main-text {
    color: blue;
}
```

```html
<h1 class="title">제목1</h1>  <!-- red -->
<h1>제목2</h1>
<p class="main-text">본문1</p>  <!-- blue -->
<p>본문2</p>
```



속성(크기, 여백, 색상 같은 눈에 보이는 스타일을 지정)

크기

#### #width(가로 너비)

요소의 가로 너비를 지정

단위는 px(pixels)을 사용

```css
div {
    width: 300px;
    요소가로너비: 너비값;
}
```

#### #height(세로 너비)

요소의 세로 너비를 지정

```css
div {
    height: 150px;
    요소세로너비: 너비값;
}
```

F12 로 확인



#### #font-size(글자 크기)

요소 내용(Text)의 글자 크기를 지정

대부분의 브라우저 글씨크기 기본이 16px



여백

#### #margin(요소의 바깥 여백)

요소의 바깥 여백 지정

바깥 여백은 요소와 요소 사이의 여백(거리, 공간)을 생성할 때 사용

```css
div {
    margin: 20px;
    요소바깥여백: 여백값;
}
```

위 코드는 margin 은 요소의 위, 아래, 좌, 우 모두 20px 의 여백을 지정하겠다는 의미

세분화하기 위해 아래와 같이 한 방향씩 지정할 수도 있다.

개별속성(합친건 단축속성)

```css
div {
    margin-top: 20px;
    margin-right: 20px;
    margin-bottom: 20px;
    margin-left: 20px;
    요소바깥여백-위쪽: 여백값;
    요소바깥여백-오른쪽: 여백값;
    요소바깥여백-아래쪽: 여백값;
    요소바깥여백-왼쪽: 여백값;
}
```



#### #padding(요소의 내부 여백)

요소의 내부 여백을 지정

내부 여백은 자식 요소를 감싸는 여백을 의미

```css
div {
    padding: 20px;
    요소내부여백: 여백값;
}
```

margin 과 같이 한 방향씩 지정할 수 있다.

```css
div {
    padding-top: 20px;
    padding-right: 20px;
    padding-bottom: 20px;
    padding-left: 20px;
    요소내부여백-위쪽: 여백값;
    요소내부여백-오른쪽: 여백값;
    요소내부여백-아래쪽: 여백값;
    요소내부여백-왼쪽: 여백값;
}
```



색상

#### #color(글자 색상)

요소 내용(Text) 의 글자 색상을 지정

font-color, text-color 없음

```css
div {
    color: red;
    글자색상: 빨강;
}
```



#### #background(요소 색상)

요소의 배경 색상을 지정

color 는 글자의 색만 지정할 수 있으며, 요소의 (배경)색을 바꾸려면 background-color(개별 속성) 가 필요

```css
div {
    background-color: red;
    요소배경: 빨강;
}
```

