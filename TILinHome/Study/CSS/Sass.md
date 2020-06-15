# Sass

Syntactically Awesome Style Sheets : 짱 멋진 스타일시트

CSS pre-processor(CSS 를 확장하는 스크립팅 언어. 컴파일러를 통해 브라우저에서 사용할 수 있는 일반 CSS 문법 형태로 변환)로서, 복잡한 작업을 쉽게, 코드의 재활용성을 높여주고 코드의 가독성을 높여주어 유지보수를 쉽게 해준다.



어떻게 컴파일?

* 오리지널 Ruby Sass 사용

  `gem install sass` 로 설치하고,

  `sass style.scss style.css` 로 컴파일

* GUI 어플리케이션 사용 - Koala, Hammer, Compass 등

* libsass 사용

  C언어로 작성된 매우 빠른 Sass compiler. 많은 환경에서 사용될 수 있음

* 학습용 https://www.sassmeister.com/



.SASS 와 .SCSS 의 차이

SCSS 는 CSS 의 상위집합으로서, CSS 와 동일한 문법으로 SASS 의 특별한 기능들이 추가되어있음



### Comment (주석)

```sass
// 한줄 주석
/* You can see me */
/*
you
can
see
me
*/
```



### Variable(변수)

Sass 는 CSS 에 변수 개념을 도입해준다.

변수로 사용 가능한 형태 : 숫자, 문자열, 폰트, 색상, null, lists, maps

변수 사용 시 `$` 문자 사용

```Sass
$primary-color: #333;
```

