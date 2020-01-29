var app = new Vue ({
    el: '#app',
    data: {
        message:'Hello Vue.js!',
        list: ['사과', '바나나', '딸기'],
        show: true
    },
    methods: {
        handleClick: function(event) {
            alert(event.target)  // [object HTMLButtonElement]
        }
    }
})