### MVVM 모델에서의 Vue

MVVM 패턴의 뷰모델(ViewModel) 레이어에 해당하는 화면(View)단 라이브러리

View는 브라우저에서 사용자에게 비춰지는 화면. 화면 입력박스, 버튼 등. html. html은 DOM이라는 것을 이용해서 자바스크립트로 조작. 특정 사용자가 발생하는 이벤트를 View Model 의 DOM Listeners 가 잡아서 자바스크립트에 있는 데이터를 바꿔주거나 등등 -> DataBindings 를 이용해 화면에 반영



### 기존 웹 개발 방식(HTML, Javascript)

HTML, CSS, JavaScript

auto close 플러그인

```html
    <div id="app">

    </div>
    <script>
        // jQuery선택자와 동일한
        // $('#app');
        var div = document.querySelector('#app');
        // div 태그 정보 출력
        console.log(div);
        
    </script>
```



화면에 내용 반영 안됨

```html
    <div id="app">
        <!-- hello world -->
    </div>
    <script>
        // jQuery선택자와 동일한
        // $('#app');
        var div = document.querySelector('#app');
        var str = 'hello world';

        div.innerHTML = str;

        str = 'hello world!!!';      
    </script>
```



```html
    <div id="app">
        <!-- hello world -->
    </div>
    <script>
        // jQuery선택자와 동일한
        // $('#app');
        var div = document.querySelector('#app');
        var str = 'hello world';

        div.innerHTML = str;

        str = 'hello world!!!';     
        div.innerHTML = str; 
    </script>
```

div 태그에 바뀐 문자열 정보를 대입해서 쓰고 저장해야 갱신됨

일반적인 웹 개발 방식

위와 같은 개발 패턴을 Vue.js Reactivity 구현해서 

```html
    <div id="app"></div>

    <script>
        var div = document.querySelector('#app');
        div.innerHTML = 'hello world';
    </script>
```

mdn object define property 구글링

`Object.defineProperty()` 는 객체의 동작을 재정의하는 api



개발자 도구에서

`var a = 10;`

a라는 변수를 만들고 10을 대입.

a에 10 할당

`a`  // 10 접근된 값 확인

`a = 20;`  // 20 할당된 값 바뀜

객체를 선언하고 값을 할당. 할당과 접근.



특정 변수의 동작, 더 나아가 객체의 특정 속성의 동작을 재정의하는 것이 

```html
    <div id="app"></div>

    <script>
        var div = document.querySelector('#app');
        var viewModel = {};

        // Object.defineProperty(대상 객체, 객체의 속성, {
        //     // 정의할 내용
        // })

        Object.defineProperty(viewModel, 'str', {
            // 속성에 접근했을 때의 동작을 정의
            get: function() {
                console.log('접근');                
            },
            // 속성에 값을 할당했을 때의 동작을 정의
            set: function(newValue) {
                console.log('할당', newValue);
                div.innerHTML = newValue;
            }
        })
    </script>
```

반응성. 

vue.js의 핵심은 데이터의 변화를 라이브러리에서 감지해서 알아서 화면을 자동으로 그려줌

데이터 바인딩.







