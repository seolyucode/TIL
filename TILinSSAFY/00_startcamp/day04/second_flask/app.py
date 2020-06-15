import datetime

from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/add')
def add():
    #pass  # add.html => <input> * 2
    return render_template('add.html')


@app.route('/substr')
def substr():
    return render_template('review.html')
    

# @app.route('/result')
# def result():
#    #pass  # result.html => input_data 의 합
#    num1 = request.args.get('num1')
#    num2 = request.args.get('num2')
#    result = int(num1) + int(num2)

#    return render_template('result.html', result=result)

@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)

    return render_template('result.html', result=result)
    

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    print(request.headers)
    return render_template('send.html')


# POST는 취급주의. args아닌 form(박스). 비밀번호 날릴 때 씀. methods=['POST', 'GET'] 2개 이상 쓸 수 있음
@app.route('/receive', methods=['POST'])
def receive():
    data = request.form.get('msg')
    token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
    stock = Stock(data, token = token).get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']
    # print(stock.get_quote())

    # print(request.args)
    # data = request.args.get('msg')

    # return render_template('receive.html', data=data)
    # return render_template('receive.html', stock=stock)
    return render_template(
        'receive.html', 
        c_name=company_name,
        l_price=latest_price
        )


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    #return f'SSAFY 2기 1학기 종료일까지 {left.days} 일 남았습니다 ♪ *҉＼( ˆᴗˆ )ﾉ✩'
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '라이온 킹',
        '진범'
    ]
    return render_template('boxoffice.html', movies=top_5)

if __name__ == '__main__':
    app.run(debug=True)
