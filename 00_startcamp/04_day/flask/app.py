from flask import Flask, render_template, request #플라스크에서 플라스크, 렌더 템플릿 임포~ㄹ트
from datetime import datetime 
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html') #템플릿 렌더링


@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'


@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now() #today_time 에 오늘날짜 입력
    # 수료 날짜
    endgame = datetime(2019, 11,29) #endgame에 수료날짜 입력
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다</h1>
    <ul>
        <li>1번</li> #번호없는
        <li>2번</li>
    </ul>

    """

@app.route('/greeting/<string:name>') #<(string:_기본값으로 생략가능, 다른 형에서는 사용해야함)변수명>
# @app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다. {name}'
    return render_template('greeting.html', html_name = name)

@app.route('/cube/<int:number>')
def cube(number):
    # 연산을 모두 끝내고 변수만 cube.html 로 넘긴다
    result = number**3
    # return f'{number}의 세제곱은 {number**3}입니다.'
    return render_template('cube.html', result = result, number = number)


@app.route('/lunch/<int:count>')
def lunch(count):
    menu = ['부대찌개', '곱창', '삼계탕', '대창', '양말', '신발', '햄버거']
    choice = random.sample(menu,count)
    return f'{choice}.'
    

@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨 : 파 프롬 홈', '알라딘', '기생충', '엔드게임']
    return render_template('movie.html', movies=movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    print(request.args)
    name = request.args.get('data')
    return render_template('pong.html', name=name)

    #https://search.naver.com/search.naver?query=
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/receive')
def receive():
        person = ['체력', '건강', '피곤', '힘듦', '졸림' , '활기']
        choice = random.sample(person,3)
        name = request.args.get('data')
        return render_template('receive.html',choice=choice, name = name)