new Vue({
    el: '#app',
    data: {
        myChoice: null,
        comChoice: null,
        count: 3,
        winner: null,
        lifeOfMe: 3,
        lifeOfCom: 3,
        isSelectable: true,
        logs: []
    },
    watch: {
        count: function (newVal) {
            if(newVal === 0) {
                // Math.random() 0.33, 0.66, 그 외 나머지
                let number = Math.random()
                if(number < 0.33) {
                    this.comChoice = 'scissor'
                } else if(number < 0.66) {
                    this.comChoice = 'rock'
                } else {
                    this.comChoice = 'paper'
                }
                // 가위바위보 승패 결정
                if(this.myChoice === this.comChoice) this.winner = 'no one'
                else if(this.myChoice === 'rock' && this.comChoice === 'scissor') this.winner = 'me'
                else if(this.myChoice === 'scissor' && this.comChoice === 'paper') this.winner = 'me'
                else if(this.myChoice === 'paper' && this.comChoice === 'rock') this.winner = 'me'
                else if(this.myChoice === 'scissor' && this.comChoice === 'rock') this.winner = 'com'
                else if(this.myChoice === 'paper' && this.comChoice === 'scissor') this.winner = 'com'
                else if(this.myChoice === 'rock' && this.comChoice === 'paper') this.winner = 'com'
                else this.winner = 'error'

                // 몫 차감
                if(this.winner === 'me') {
                    this.lifeOfCom --
                }
                else if(this.winner === 'com') {
                    this.lifeOfMe --
                }
                this.count = 3
                // 버튼은 다시 보이게 됨
                this.isSelectable = true

                let log = {
                    message: `You: ${this.myChoice}, Computer: ${this.comChoice}`,
                    winner: this.winner
                }
                // push와 달리 가장 최근 것이 앞으로 들어감. 최근 로그 가장 앞에
                this.logs.unshift(log)
            }
        },
        lifeOfMe: function(newVal) {
            if(newVal === 0) {
                setTimeout(() => {
                    confirm('안타깝네요. 당신이 패배하였습니다.')
                    this.lifeOfMe = 3
                    this.lifeOfCom = 3
                    this.myChoice = null
                    this.comChoice = null
                    this.winner = null
                    this.logs = []
                }, 500)
            }
        },
        lifeOfCom: function(newVal) {
            if(newVal === 0) {
                setTimeout(() => {
                    confirm('축하드립니다. 당신이 승리하였습니다.')
                    this.lifeOfMe = 3
                    this.lifeOfCom = 3
                    this.myChoice = null
                    this.comChoice = null
                    this.winner = null
                    this.logs = []
                }, 500)
            }
        }
    },
    methods: {
        startGame: function() {
            // 버튼이 보이지 않음
            this.isSelectable = false
            if(this.myChoice === null) {
                alert('가위 바위 보 중 하나를 선택해주세요.')
            } else {
                let countDown = setInterval(()=> {
                    this.count --
                    if(this.count === 0) {
                        clearInterval(countDown)
                    }
                }, 1000)
            }
        }
    }
})