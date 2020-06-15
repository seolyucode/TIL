header tag mdn 구글링

footer tag mdn

h1 tag mdn

html 구조 css 표현

h1 ~ h6 는 구조 나타내는 용도. CSS의 font-size 속성으로 폰트 크기 조정

h1 은 한 페이지에 하나만 사용



 https://heropy.blog/2019/05/26/html-elements/ 

main

article 독립적으로 구분되거나 재사용 가능한 영역을 설정.(매거진/신문 기사, 블로그 등)

section 문서의 일반적인 영역 설정

aside 문서의 별도 콘텐츠를 설정(광고, 기타 링크 등의 사이드바Side bar 설정)

nav 다른 페이지 링크를 제공하는 영역(Navigation, 보통 메뉴(Home, About, Contact), 목차, 색인 등 설정)



일반적으로 영역을 설정하는 요소는 블록 요소



address

div 본질적으로 아무것도 나타내지 않는 콘텐츠 영역 설정(Division, 꾸미는 목적)



문자 콘텐츠

ol 정렬된 목록

ul 정렬되지 않은 목록

li 단독으로 사용할 수 없으며, ol 이나 ul 에 자식으로 포함되어야 함



용어(<dt>)와 정의(<dd>) 쌍들의 영역(<dl>)을 설정

(Description List, Definition Details, Definition Term)

.. <dl> 은 <dd>, <dt> 만을 포함해야 함

키(key) / 값(value) 형태를 표시할 때 유용

```html
<dl>
    <dt>Coffee</dt>
    <dd>Coffee is a brewed drink prepared from roasted .. species.</dd>
    <dt>Milk</dt>
    <dd>Milk is a nutrient-rich, white liquid food ... </dd>
</dl>

<ul>
    <li>
        <dfn>Coffee</dfn>
        <p>Coffee is a brewed drink prepared from roasted .. species.</p>
    </li>
    <li>
        <dfn>Milk</dfn>
        <p>Milk is a nutrient-rich, white liquid food ... </p>
    </li>
</ul>
```



p 하나의 문단을 설정 (Paragraph)



hr <hr /> 문단의 분리(주제에 의한)를 위해 설정 (Horizontal Rule)

대부분의 경우 수평선(border)으로 표시(표현적 관점)되나 의미적 관점으로만 사용해야 함.

```css
hr {
    border: 2px dashed red;
    padding: 20px;
}
```

사각형 

```css
hr {
   border: none;
   border-top:2px dashed red;
}
```



줄바꿈 <br/>



pre 서식이 미리 지정된 텍스트를 설정. (Preformatted Text)

* 텍스트의 공백과 줄바꿈을 유지하여 표시할 수 있음.
* 기본적으로 Monospace 글꼴 계열로 표시됨.

```html
<pre>동해물과   백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세.</pre>
```



blockquote 일반적인 인용문을 설정(Block Quotation)

```html
<blockquote cite="URL">
인용문
</blockquote>
```

