MarkDown 사용법

.md  <=  마크다운 문법으로 작성된 파일



마크다운의 장점

1. 문법이 쉽다
2. 관리가 쉽다
3. 지원 가능한 플랫폼과 프로그램이 다양하다

마크다운의 단점

1. 표준이 없어서 사용자마다 문법이 상이할 수 있다
2. 모든 HTMl 마크업을 대신하지 못한다



메모장~전용 에디터

Atom, 일반 블로그, 워드프레스, Slack, Trello

화면에 표현되는 스타일(CSS)은 설정에 따라 달라짐

HTML과 마찬가지로 눈에 보이는 스타일은 무시하고 각 문법의 의미로 사용





### 마크다운 문법(syntax)

#### 제목(Header)

```
<h1> 부터 <h6> 까지 제목 표현
```

```mark
# 제목 1
## 제목 2
### 제목 3
#### 제목 4
##### 제목 5
###### 제목 6
```



#### 강조(Emphasis)

```
각각 <em>, <strong>, <del> 태그로 변환됨
밑줄 <u></u>
```

```
이텔릭체는 *별표(asterisks)* 혹은 _언더바(underscore)_를 사용
두껍게는 **별표(asterisks)** 혹은 __언더바(underscore)__를 사용
**_이텔릭체_와 두껍게** 같이 사용 가능
취소선은 ~~물결표시(tilde)~~를 사용
<u>밑줄</u>은 `<u></u>`를 사용
```

이텔릭체는 *별표(asterisks)* 혹은 _언더바(underscore)_를 사용
두껍게는 **별표(asterisks)** 혹은 __언더바(underscore)__를 사용
**_이텔릭체_와 두껍게** 같이 사용 가능
취소선은 ~~물결표시(tilde)~~를 사용
<u>밑줄</u>은 `<u></u>`를 사용



#### 목록(List)

```
<ol>, <ul> 목록 태그로 변환
```

```
1. 순서가 필요한 목록
1. 순서가 필요한 목록
 - 순서가 필요하지 않은 목록(서브)
 - 순서가 필요하지 않은 목록(서브)
1. 순서가 필요한 목록
 1. 순서가 필요한 목록(서브)
 1. 순서가 필요한 목록(서브)
1. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호
 - 대쉬(hyphen)
 * 별표(asterisks)
 + 더하기(plus sign)
```



#### 링크(Link)

```
<a> 로 변환됨
```

```
[GOOGLE](https://google.com)
[NAVER](https://naver.com "링크 설명(title)을 작성하세요.")
[상대적 참조](../user/login)
[Dribbble][Dribbble link]
[GitHub][1]

문서 안에서 [참조 링크]를 그대로 사용할 수도 있음

다음과 같이 문서 내 일반 URL이나 꺾쇠 괄호(`<>`, Angle Brackets)안의 URL은 자동으로 링크를 사용
구글 홈페이지: https://google.com
네이버 홈페이지: <https://naver.com>
  
[Dribbble link]: https://dribbble.com
[1]: https://github.com
[참조 링크]: https://naver.com "네이버로 이동합니다"
```

<a href="https://google.com" target="_blank">구글</a>

[구글][google url]

[google url]: https://google.com



#### 이미지(Images)

```
<img> 로 변환됨
링크와 비슷하지만 앞에 !가 붙음
```

```
![대체 텍스트(alternative text)를 입력](이미지 주소 "링크 설명(title) 작성")
![로고][logo]
[logo]: https://seolyucode.github.io/imgs/korea.png "태극기"
```

![로고][logo]

[logo]: https://seolyucode.github.io/imgs/korea.png "태극기"



#### 코드(Code) 강조

```
<pre>, <code> 로 변환됨
숫자 1번 키 왼쪽에 있는 `(Grave)를 입력
```



##### 인라인(inline) 코드 강조

```
`background` 혹은 `background-image` 속성으로 요소에 배경 이미지를 삽입할 수 있음
```

`background` 혹은 `background-image` 속성으로 요소에 배경 이미지를 삽입할 수 있음



#### 블록(block) 코드 강조

```
` 을 3번 이상 입력하고 코드 종류도 적음
```

```html
<a href="https://seolyucode.github.io/" target="_blank">내 블로그</a>
```

```javascript
function func() {
    var a = 'AAA';
    return a;
}
```



#### 표(Table)

```
<table> 태그로 변환됨
헤더 셸을 구분할 때 3개 이상의 - (hyphen/dash) 기호가 필요
헤더 셸을 구분하면서 : (Colons) 기호로 셸 (열/칸) 안에 내용을 정렬할 수 있음
가장 좌측과 가장 우측에 있는 | (vertical bar) 기호는 생략 가능
```

```
| 값 | 의미 | 기본값 |
|---|:---:|---:|
| `static` | 유형(기준) 없음 / 배치 불가능 | `static` |
| `relative` | 요소 자신을 기준으로 배치 |  |
| `absolute` | 위치 상 부모(조상)요소를 기준으로 배치 | |
| `fixed` | 브라우저 창을 기준으로 배치 | |


값 | 의미 | 기본값
---|:---:|---:
`static` | 유형(기준) 없음 / 배치 불가능 | `static`
`relative` | 요소 자신을 기준으로 배치 |
`absolute` | 위치 상 부모(조상)요소를 기준으로 배치 |
`fixed` | 브라우저 창을 기준으로 배치 |
```

| 값         |                  의미                  |   기본값 |
| ---------- | :------------------------------------: | -------: |
| `static`   |     유형(기준) 없음 / 배치 불가능      | `static` |
| `relative` |       요소 자신을 기준으로 배치        |          |
| `absolute` | 위치 상 부모(조상)요소를 기준으로 배치 |          |
| `fixed`    |      브라우저 창을 기준으로 배치       |          |



#### 인용문(BlockQuote)

`<blockquote>` 태그로 변환

```
인용문(blockQuote)
> 남의 말이나 글에서 직접 또는 간접으로 따온 문장
> _(네이버 국어 사전)_

BREAK!

> 인용문을 작성하세요
>> 중첩된 인용문(nested blockquote)을 만들 수 있다
>>> 중중첩된 인용문 1
>>> 중중첩된 인용문 2
>>> 중중첩된 인용문 3
```

인용문(blockQuote)
> 남의 말이나 글에서 직접 또는 간접으로 따온 문장
> _(네이버 국어 사전)_

BREAK!

> 인용문을 작성하세요
> > 중첩된 인용문(nested blockquote)을 만들 수 있다
> > > 중중첩된 인용문 1
> > > 중중첩된 인용문 2
> > > 중중첩된 인용문 3



원시 HTML (Raw HTML)

마크다운 문법이 아닌 원시 HTML 문법을 사용할 수 있음

```html
<u>마크다운에서 지원하지 않는 기능</u>을 사용할 때 유용하며 대부분 잘 동작
<img width="150" src="https://seolyucode.github.io/imgs/korea.png" alt="태극기" title="Korea">
![태극기](https://seolyucode.github.io/imgs/korea.png)
```



<u>마크다운에서 지원하지 않는 기능</u>을 사용할 때 유용하며 대부분 잘 동작
<img width="150" src="https://seolyucode.github.io/imgs/korea.png" alt="태극기" title="Korea">
![태극기](https://seolyucode.github.io/imgs/korea.png)