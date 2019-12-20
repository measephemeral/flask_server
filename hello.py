from flask import Flask, escape, request, render_template
import random
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!!!'


@app.route('/myname')
def myname():
        return '문준호입니당'

# 랜덤으로 점심메뉴 추천해주는 서버
@app.route('/lunch')
def lunch():
    menus = ['양자강','김밥카페','20층','순남시래기']
    lunch = random.choice(menus)
    return lunch

@app.route('/hibiki')
def hibiki():
    songs = ['RainbowFlower','G-Beat','꽃피는 용기','Little Miracle']
    hibiki = random.choice(songs)
    return hibiki

#아이돌 백과사전..?

@app.route('/idol')
def idol():
    idols = {
        '뉴제네':{
        '혼다 미오': 15,
        '시마무라 우즈키': 17,
        '시부야 린': 15
        },
        '142s':{
        '코시미즈 사치코':'더 귀여움',
        '시라사카 코우메':'호러돌',
        '호시 쇼코':'메탈 버섯'
        },
        'BCG':['린제','쥬리','치요코','카호','나츠하']
    }
    return idols

@app.route('/post/<int:num>')
def post(num):
    posts = ['0번 포스트','1번 포스트','2번 포스트']
    return posts[num]

#실습
@app.route('/cube/<int:num>')
def cube(num):
    cubed = num*num*num
    return str (cubed)

# 클라이언트에게 html 파일을 전달
@app.route('/html')
def html():
    return render_template('hello.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    # age = request.args['age']
    return render_template('pong.html',age_in_html=age)

#로또 번호를 가져와서 보여주는 서버
@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    result = requests.get(url).json()

    winner = []
    for i in range(1,7):
        winner.append(result.get(f'drwtNo{i}'))

    winner.append(result.get('bnusNo'))

    return json.dumps(winner)

#https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=회차번호

# 시동키: env FLASK_APP=hello.py flask run
app.run(debug=True)