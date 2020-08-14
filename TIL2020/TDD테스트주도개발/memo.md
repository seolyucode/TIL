단위 테스트 (Unit Test)



단위(Unit): 특정 조건에서 어떻게 작동해야 할지 정의한 것. 대게 '함수'로 표현

준비(arrange), 실행(act), 단언(assert) 패턴을 따른다



테스트 주도개발 (TDD)

적색(Red), 녹색(Green), 리팩터(Refactor) 순환

테스트하기 쉬운 코드

관심사의 분리



설치

재스민 프레임웍을 설치하고 TDD 개발 환경을 꾸미자

1. 스탠드얼론 (standalone)
2. 카르마(karma)와 함께 설치하는 방법 (자동화) <-실무



https://github.com/jasmine/jasmine/releases

2.7.0

 압축 풀고 SpecRunner.html 실행

자스민 라이브러리 파일

소스 코드

테스트 코드



테스트 러너(Test Runner)란

* 재스민, 소스, 테스트 코드를 실행
* 스탠드 얼론으로 설치한 자스민은 HTML 파일이 테스트 러너임
* (테스트 자동화를 하려면 테스트러너인 카르마(Karma)와 함께 사용 가능)

`git checkout -f install-jasmine`



테스트 꾸러미 (Test Suite)

* describe('테스트 설명', 테스트 구현 함수)

테스트 스펙 (Test Spec)

* it ('테스트 설명', 기대식을 가진 테스트 구현 함수)

기대식과 매쳐

* expect(결과 값).toBe(기대하는 값)

스파이

* spyOn(감시할 객체, 감시할 메소드)



어떻게 하면 테스트할 수 있을까?

1. 코드를 UI에서 완전히 분리

   HTML에서 JS 코드를 떼어내면 비즈니스 로직만 테스트할 수 있음

2. 자바스크립트를 별도 파일로 분리

   다른 곳에서도 재사용할 수 있고 테스트성도 좋아짐



모듈 패턴

함수로 데이터를 감추고, 모듈 API를 담고 있는 객체를 반환하는 형태

(자바스크립트에서 가장 많이 사용되는 패턴)

1. 임의 함수를 호출하여 생성하는 모듈과
2. 즉시 실행 함수(IIFE) 기반의 모듈이 있다  // 함수 선언 즉시 실행한다. 싱글톤



모듈 생성 원칙

1. 단일 책임 원칙에 따라 모듈은 한 가지 역할만 한다

   그 역할만 집중 -> 모듈을 더욱 튼튼하게 만들고 테스트하기도 쉽다

2. 모듈 자신이 사용할 객체가 있다면 의존성 주입 형태로 제공

   또는 팩토리 주입형태로 제공

   테스트하기도 쉽다



클릭 카운터 모듈

ClickCounter는 카운터 데이터를 다루는 모듈이다

전역 공간에 있는 counter 변수를 ClickCounter 안에서 관리하자

첫번째 스펙

"ClickCounter 모듈의 getValue()는 카운터 값을 반환"

`git checkout --force ClickCounter-spec-1`

force 옵션은 현재 코드 변경사항을 다 무시하고 브랜치를 이동



테스트 코드가 있기 때문에 안심하고 리팩토링 가능

하나의 기능에 대해 Red - Green - Refactor 사이클로 개발



두번째 스펙

"ClickCounter 모듈의 increase()는 카운터 값을 1만큼 증가한다"

`git checkout --force ClickCounter-spec-2`



beforeEach는 it 함수 호출 직전에 실행되는 자스민 함수

```javascript
describe(()=> {
    beforeEach(()=> { // 1
    afterEach(()=> { // 3
    it(()=> { // 2
    })})})
})
// 중복코드를 beforeEach로 옮기자
```

중복 코드 제거 => DRY한 테스트 코드가 됨

 Do not Repeat Yourself



클릭 카운트 뷰 모듈

카운터 데이터는 돔(DOM)에 반영되어야 한다

이 역하를 하는 ClickCountView 모듈을 만들자

데이터를 출력하고 이벤트 핸들러를 바인딩하는 일을 담당할 것



첫번째 스펙

"ClickCountView 모듈의 updateView()는 카운트 값을 출력"

`git checkout --force ClickCountView-spec-1`

데이터를 조회할 ClickCounter를 어떻게 얻지

데이터를 출력할 돔 엘레먼트는 어떻게 테스트 하지

주입하자

* ClickCounter는 객체를 만들어 파라매터로 전달 받자
* 데이터를 출력할 돔 엘레먼트도 만들어 전달 받자

TDD 방식으로 사고하다 보면

이런식으로 필요한 모듈을 주입받아 사용하는 경향이 생김

하나의 기능 단위로 모듈을 분리할 수 있기 때문에

단일 책임 원칙을 지킬 수 있다



ClickCountView에 의존성 주입이 되었는지 어떻게 체크하지

expect(function() { throw new Error()}).toThrowError()



두번쨰 스펙

"ClickCountView 모듈의 increaseAndUpdateView()는 카운트 값을 증가하고 그 값을 출력"

`git checkout --force ClickCountView-spec-2`

```javascript
describe('App.ClickCountView 모듈의', ()=> {
    describe('increaseAndUpdateView()는', ()=> {
        it('카운트 값을 증가하고 그 값을 출력한다', ()=> {
            
        })
    })
})
```

카운트 값을 증가하고 그 값을 출력한다? (사실은 두개임)

* ClickCounter의 increase 함수를 실행
* updateView 함수를 실행



테스트 더블

단위 테스트 패턴으로,

테스트하기 곤란한 컴포넌트를 대체하여 테스트하는 것

특정한 동작을 흉내만 낼 뿐이지만 테스트 하기에는 적합



다음 5가지를 통칭하여 테스트 더블이라고 함

더미(dummy): 인자를 채우기 위해 사용

스텁(sturb): 더미를 개선하여 실제 동작하게끔 만든 것. 리턴값을 하드 코딩한다

스파이(spy): 스텁과 유사. 내부적으로 기록을 남기는 추가기능

페이크(fake): 스텁에서 발전한 실제 코드. 운영에서는 사용할 수 없음

목(mock): 더미, 스텁, 스파이를 혼합한 형태



자스민에서는 테스트 더블을 스파이스(spies)라고 부른다



spyOn(), createSpy() 함수를 사용할 수 있다



```javascript
//clickCounter 모듈의 increase 함수를 감시하도록 설정

spyOn(MyApp, 'foo')



// 특정 행동을 한 뒤

bar()



// 감시한 함수가 실행되었는지 체크

expect(MyApp.foo).toHaveBeenCalled()



즉, bar() 함수가 MyApp.foo() 함수를 실행하는지 검증하는 코드
```



세번째 스펙

"클릭 이벤트가 발생하면 increaseAndUpdateView()를 실행한다"

`git checkout --force ClickCountView-spec-3`



(카운터 값을 출력할 돔 엘리먼트(updateEl)를 주입했듯이)

클릭 이벤트 핸들러(increateAndUpdateView)를 바인딩할 돔 엘리멘트(triggerEl)를 주입하자



화면에 붙여보자

`git checkout --force index.html-1`



"ClickCounter 모듈은 '데이터'를 주입 받는다"

`git checkout -f ClickCounter-spec-3`



네번째 스펙

"ClickCounter 모듈의 increase 함수는 대체될 수 있다"



값을 올릴수도(increase) 있지만 내릴수도 있어야 한다

이름변경: increase -> count

`git checkout -f ClickCounter-spec-4`



`git checkout -f index.html-3`



자바스크립트 개발에는 독특한 마음가짐을 가져야

컴파일러가 없는한 테스트가 최선

테스트주도개발 (TDD)

SOLID하고 DRY한 코드 (Counter, CounterView)

견고한 어플리케이션을 만들 수 있다