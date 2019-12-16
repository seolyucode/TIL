## HTML - 블록 레벨(Block level) 요소와 인라인(Inline) 요소

1. 블록 요소
   1. DIV, H1, P
   2. 사용 가능한 최대 가로 너비를 사용한다.
   3. 크기를 지정할 수 있다.
   4. (width: 100%; height: 0; 로 시작)
   5. 수직으로 쌓임
   6. margin, padding 위, 아래, 좌, 우 사용 가능
   7. 레이아웃
2. 인라인 요소
   1. SPAN, IMG
   2. 필요한 만큼의 너비를 사용한다.
   3. 크기를 지정할 수 없다.
   4. (width: 0; height: 0; 로 시작)
   5. 수평으로 쌓임
   6. margin, padding 위, 아래는 사용을 할 수 없다.
   7. TEXT

```html
div { display: block; }
h1 { display: block; }
p { display: block; }

span { display: inline; }
```



```html
EUC-KR: 완성형
	한글 깨지는 현상 생김
	박 영 웅
UTF-8: 조합형
	ㅂ ㅏ ㄱ ㅇ ㅕ
```



html 요소 레퍼런스 mdn 구글링

meta tag mdn 구글링



메타데이터 - LINK



style tag mdn



mine type mdn



base tag mdn

base 태그는 html 문서 내에서 한번만 작성 가능하므로 주요하게 쓰일 경로 입력

 