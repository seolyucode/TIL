import Vue from 'vue'
import App from './App.vue'
import router from './router'  // 폴더를 가지고온게 아니고
// index.js에서 export 하는 것을 router 에 담아달라는 의미?
// import router from './router/index.js'  .js 생략 가능하고 폴더 안에 파일이 있고 파일 이름이 index이면 안써도 알아서 찾음. 
import VueSession from 'vue-session'  // 발급받은 Token 을 SessionStorage 에 저장하는걸 도와줌.

Vue.config.productionTip = false;
Vue.use(VueSession);  // Vue 에게 VueSession 이라는 Middleware 등록

new Vue({
  router,  // router: router,  // router/index.js 에서 악수 하고, 본격적으로 일을 시작.
  render: h => h(App)
}).$mount('#app')
