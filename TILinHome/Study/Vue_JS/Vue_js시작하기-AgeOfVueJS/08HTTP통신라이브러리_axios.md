### HTTP 라이브러리와 Ajax 그리고 Vue Resource

Ajax(Asynchronous JavaScript and XML, 에이잭스) : 비동기적인 웹 애플리케이션의 제작

Ajax 를 함으로 인해서 뷰 라우터 라든지 싱글 페이지 애플리케이션이 조금 더 구현하기 쉬워졌다

일반적으로 많이 쓰는 jQuery.ajax()  <- jQuery에서는 ajax를 이용해서 데이터를 호출하고 받아오고 수정하고 등등의 일 많이 함 



axios

vue resource github 구글링 -> The HTTP client for Vue.js 예전 공식 라이브러리. 안씀



#### 엑시오스 <- 뷰에서 권고하는 HTTP 통신 라이브러리

Axios <- Promise 기반의 HTTP 통신 라이브러리. Promise 기반의 HTTP 통신 라이브러리. 상대적으로 다른 HTTP 통신 라이브러리들에 비해 문서화가 잘되어있고 API가 다양



[axios](https://github.com/axios/axios) github 구글링



오픈소스 사용방법 기준 <- Star 수, commits, contributors 수, 언제/최근에 수정되었는지



Promise(자바스크립트의 비동기 처리 패턴) based HTTP client for the browser and node.js



자바스크립트의 비동기 처리 패턴

1. [callback](https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/)
2. [promise](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)
3. promise + generator
4. [async & await](https://joshua1988.github.io/web-development/javascript/js-async-await/)



```html
<div id="app">
    <!-- 버튼 클릭했을 때 getData라는 method 호출하기 -->
	<button v-on:click="getData">get user</button>
<div>

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    new Vue({
        el: '#app',
        methods: {
            getData: function() { 
                // axios.get 에서 url 참고하고 있음
                // url 가보면 10개의 사용자 정보가 담긴 배열
                // jsonplaceholder
                // 자바스크립트로 api를 요청할 때 테스트 해볼 수 있는 사이트
                // 버튼 눌렀을 때 10개의 유저 정보를 받아오고나서
                axios.get('https://jsonplaceholder.typicode.com/users/')
                	// 성공하면 then(promise 참고)
                    .then(function(response) {
                    console.log(response);
                    
                })
                	// 실패하면 catch
                    .catch(function(error) {
                    console.log(error);
                });
            }
        }
    })
</script>
```

![1](C:./imgs/1.png)

get user 버튼 누르면 데이터가 옴

서버로 갔다가 온 데이터의 결과

![2](C:./imgs/2.png)

config, data, headers, request 속성들은 axios의 일반적인 구조

![3](C:./imgs/3.png)

필요한 것은 데이터 속성 안에 10개의 사용자 정보

```html
    <script>
        new Vue({
            el: '#app',
            methods: {
                getData: function() { 
                    axios.get('https://jsonplaceholder.typicode.com/users/')
                        .then(function(response) {
                        console.log(response.data);  // 이렇게 바꾸고
                    })
                        .catch(function(error) {
                        console.log(error);
                    });
                }
            }
        })
    </script>
```

데이터가 배열로 넘어온다

![4](C:./imgs/4.png)

```html
<script>
    new Vue({
        el: '#app',
        data: {
            // users 빈 배열에 받아온 배열 넣을것임
            users: []
        },
        methods: {
            getData: function() { 
                axios.get('https://jsonplaceholder.typicode.com/users/')
                    .then(function(response) {
                    console.log(response.data);
                    // this.users 가 data 속성에 정의한 users 일까
                    this.users = response.data;
                })
                    .catch(function(error) {
                    console.log(error);
                });
            }
        }
    })
</script>
```

![5](C:./imgs/5.png)

Esc 누르면 data 내용과 console 같이 보임

get user 버튼 누르면

![6](C:./imgs/6.png)

그런데 users는 아직 0 이다. 빈 배열

```html
<script>
    new Vue({
        el: '#app',
        data: {
            users: []
        },
        methods: {
            getData: function() { 
                // 호출하기 전 this는 기본적인 인스턴스나 컴포넌트를 바라보는 this
                this
                axios.get('https://jsonplaceholder.typicode.com/users/')
                    .then(function(response) {
                    console.log(response.data);
                    // 여기서(호출하고 비동기처리에 의해서 들어오는 콜백함수)의 this는 
                    // axios 코드를 호출하기 전 this와 다르다
                    // console.log(this); 해보기
                    this.users = response.data;
                })
                    .catch(function(error) {
                    console.log(error);
                });
            }
        }
    })
</script>
```

[자바스크립트 동작 원리](https://joshua1988.github.io/web-development/translation/javascript/how-js-works-inside-engine/)



해결책

```html
<script>
    new Vue({
        el: '#app',
        data: {
            users: []
        },
        methods: {
            getData: function() { 
                var vm = this;  // vm 은 뷰모델 약자. 인스턴스를 가리키는 약어로 많이 쓰임(추후 ES6 / 화살표 함수 배우면 vm 대신에 this로 바로 연결하는 방법 알게됨)
                axios.get('https://jsonplaceholder.typicode.com/users/')
                    .then(function(response) {
                    console.log(response.data);
                    vm.users = response.data;
                })
                    .catch(function(error) {
                    console.log(error);
                });
            }
        }
    })
</script>
```

![7](C:./imgs/7.png)

get user 누르면 Console에 데이터 나오고 <Root> 누르면 갱신된 데이터 보임

![:)](C:./imgs/8.png)

아래에 담긴 데이터가 {{ user }} 에 정리되지 않은 형태로 화면에 나옴

![10](C:./imgs/10.png)

빈 배열이었다가 get user 누르면

![9](C:./imgs/9.png)



개발자도구 네트워크 패널 보는 법

![11](C:./imgs/11.png)

브라우저에서 서버로 HTTP(aixos를 이용해서 HTTP라는 프로토콜. 브라우저(클라이언트)와 서버간 데이터를 주고 받기 위한 규칙, 약속) 요청 보냄

서버에서 HTTP 응답으로 { user: 123, ... }



![12](C:./imgs/12.png)

클라이언트에서 HTTP Request를 axios로 보내기

XHR 데이터 통신 볼 수 있음

get user 눌렀을 때 HTTP Request가 서버로 날라감

![13](C:./imgs/13.png)

Headers <- HTTP의 헤더 의미. 일반적인 정보. 특정 요청에 대한 정보, 응답에 대한 정보

![14](C:./imgs/14.png)

GET 으로 보낼 때는 정보를 달라고 요청하는 것이므로

Response에 정보가 담겨져있음

![15](C:./imgs/15.png)

Preview로 보면 보기 더 수월(Response가 어떻게 구조화되어서 오는지)

![16](C:./imgs/16.png)

[Front-end 개발자가 알아야 하는 HTTP 프로토콜](https://joshua1988.github.io/web-development/http-part1/)

[구글 크롬 개발자 도구 공식 문서](https://developers.google.com/web/tools/chrome-devtools/)