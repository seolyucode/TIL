new Vue({
    el: '#app',
    data: {
        // 객체 데이터
        message: {
            value: 'Hello Vue.js!',
            scroll: 0,
            count: 0
        },
        mounted: function() {
            this.scroll = 100  // 요소의 스크롤 양 조작하기
        },
        // 배열 데이터
        list: ['사과', '바나나', '딸기'],
        // 다른 데이터를 사용해서 list에서 값을 추출하기 위한 요소
        num: 1,
        methods: {
            // 버튼을 클릭할 때의 핸들러
            increment: function() {
                this.count += 1  // 다시 할당하는 처리만 합니다.
            }
        }
    }
})