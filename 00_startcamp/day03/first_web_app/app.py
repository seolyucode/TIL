'''
# python 모듈
import random # 필통 꺼낸다

random.choice([1, 2, 3, 4, 5]) #필통에서 연필

from random import choice # 서랍 속 필통에서 연필만 꺼낸다
choice([1, 2, 3, 4, 5])
'''

from flask import Flask, render_template # flask에서 Flask, render_template만 꺼냄
import random

app = Flask(__name__)


@app.route('/')
def index():
    #return 'Hello world!'
    return render_template('index.html')

# @app.route('/hi')
# def hi():
#     return 'Hi'

@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.route('/get_lotto/<int:num>') #<int:num>에 뭐든 들어와야. 변수라우팅. 길을 뚫어주는 것
# def get_lotto_1():
#     # 1회차 로또정보


# @app.route('/hello/<name>') # var routing
# def hello(name):
#     return f'hi, {name}'

@app.route('/pick_lunch/<int:count>') # var routing
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '사천탕면',
        '쟁반짜장'
    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:num>')
def cube(num):
    return str(num ** 3)


if __name__ == '__main__':
    app.run(debug=True)

