import Vue from 'vue';  // . 안쓰면 패키지 찾고
import App from './App';  // App.vue 를 알아서 확장자 버리고 읽음 App.vue라고 써도 상관은 없음
// App.vue에서 export default 부분

new Vue({
    render: h => h(App), // 유일하게 method 인데 Arrow Function. createElement 줄여서 h
}).$mount('#app')  // el: '#app' 와 같다.