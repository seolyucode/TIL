var app = new Vue({
    // 마운트할 요소
    el: '#app',

    // 애플리케이션에서 사용할 데이터
    data: {
        message: 'Vue.js'
    },

    // 산출 속성
    computed: {
        computedMessage: function() {
            // 어떤 처리를 해서 결과 리턴하기
            return this.message + '!'
        }
    },

    // 라이프 사이클 훅
    created: function() {
        // 하고 싶은 처리
        // 이 인스턴스의 생성과 초기화가 종료되었을 때
        console.log('created')
    },

    // 애플리케이션에서 사용할 메서드
    methods: {
        myMethod: function() {
            // 하고 싶은 처리
        }
    }
})