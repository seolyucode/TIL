Vue CLI

https://cli.vuejs.org

CLI <- Command Line Interface. 명령어를 통한 특정 액션을 수행하는 도구.

Get Started -> Installation -> 

VSCode 터미널 - 새 터미널 - `node -v`

노드 버전 10 이상 확인하기

`npm -v`

6 버전 이상인거 확인하기

`npm install -g @vue/cli`



설치하는 라이브러리가 위치하는 폴더에 파일쓰기 권한 없을 때(관리자 권한 아니라서) 에러나면

`sudo npm install -g @vue/cli`



[설치된 내용들 어디?](https://stackoverflow.com/questions/5926672/where-does-npm-install-packages)



[Vue CLI 2.x]

`vue init '프로젝트 템플릿 유형' '프로젝트 폴더 위치'`

`vue init 'webpack-simple' '프로젝트 폴더 위치'`



[Vue CLI 3.x]

`vue create '프로젝트 폴더 위치'`



터미널 - 새 터미널

`vue create vue-cli`

default(babel, eslint) 엔터  <- 화살표로 이동

`cd vue-cli`

`npm run serve`

- Local: http://localhost:8080/  <- ctrl 키 누르고 클릭



`npm run serve` 라는 명령어를 보면

npm은 node package manager  <- package.json에서 dependencies, devDependencies

scripts 에 serve 에 정의된

`vue-cli-service serve` <- serve 라고 하고

`npm run serve` 하는 것이다

public 폴더에 index.html 파일

```html
<!-- built files will be auto injected -->
```

빌드된 파일들이 자동으로 추가가 될 것이라는 주석

src 폴더 밑에 정의해둔 main.js, App.vue 등등 여러가지 파일들 종합하여 최소한의 파일로 변환하여 주입

웹팩 공부하기

main.js 가보면

```javascript
new Vue({
  render: h => h(App),
}).$mount('#app')
```

```javascript
new Vue({

}).$mount('#app')

// 위 코드는 아래 코드와 같은 역할

new Vue({
    el: '#app'
})
```

```javascript
new Vue({
    el: '#app',
    render: h => h(App),
})
```

render는 뷰 내부적으로 사용하는 함수. 사용자들도 사용할 수 있는 함수.

기본적으로 template 이라는 속성을 정의했을 때 내부적으로 render 함수 실행

App 이라는 컴포넌트 즉, import 한(import App from './App.vue') 파일. .vue 라는 싱글 파일 컴포넌트 렌더

```javascript
var App = {
    template: '<div>app</div>'
}

new Vue({
    render: h => h(App),
    components: {
        'app': App
    }
}).$mount('#app')
```



.vue

싱글 파일 컴포넌트

src 폴더 우클 새파일

a.vue 생성

scf(Vetur 버전 0.22 이상은 vue) 자동완성 .vue 기본 구조 잡아줌

```vue
<template>
	<!-- HTML -->
</template>

<script>
export default {
    // Javascript
}
</script>

<style>
    /* CSS */
</style>
```

한 파일에 관리 -> 싱글 파일 컴포넌트 / .vue

```vue
var appHeader = {
	template: '<div>header</div>',
	methods: {
		addNum: function() {

		}
	}
}

<template>
	<!-- HTML -->
	<div>header</div>
</template>

<script>
export default {
    // Javascript - 인스턴스 옵션
    methods: {
		addNum: function() {

		}
	}
}
</script>

<style>
    /* CSS */
</style>
```



#### App.vue 와 HelloWorld.vue 설명

main.js 에서

import App from './App.vue'  <- App.vue 내용을 App 변수에 담음



App.vue 보면

template(HTML), script(Javascript), style(CSS)

```vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <!-- 컴포넌트 명명법 종류 -->
    <!-- <hello-world></hello-world>
    <HelloWorld></HelloWorld>
    <HelloWorld/> -->
  </div>
</template>
```

```vue
<script>
import HelloWorld from './components/HelloWorld.vue'
// 컴포넌트 내용 들고와서

export default {
  // 인스턴스 옵션 속성 or 컴포넌트 옵션 속성
  name: 'App',
  // components에 연결해서 사용
  components: {
    HelloWorld,
    'hello-world': HelloWorld,
  }
}
</script>
```



HelloWorld 컴포넌트는 components 안에 등록되어있음

HelloWorld.vue

```vue
<script>
// var appContent = {
//   props: ['propsdata']
// }

export default {
  // 인스턴스 옵션 속성
  name: 'HelloWorld',
  // props: ['msg']
  props: {
    msg: String
  }
}
</script>
```

