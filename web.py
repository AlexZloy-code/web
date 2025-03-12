from flask import Flask, render_template, request
import os


app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.</br>
Человечеству мала одна планета.</br>
Мы сделаем обитаемыми безжизненные пока планеты.</br>
И начнем с Марса!</br>
Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return """<title>Привет, Марс!</title>
    <h>Жди нас, Марс!</h><br>
    <img src="static/image/image.png" alt="здесь должна была быть картинка, но не нашлась"><br>
    <a>Вот она какая, красная планета</a>"""


@app.route('/promotion_image')
def promotion_image():
    return render_template('main.html')


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('main1.html')
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        return "Форма отправлена"
    

@app.route('/choise/<planet>')
def choise_planet(planet):
    return render_template('main2.html', planet=planet)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('main3.html', nickname=nickname, level=level, rating=rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        if os.path.exists('static/image/image_of_people.png'):
            return render_template('main4.html', img='static/image/image_of_people.png')
        return render_template('main4.html', img='static/image/base_image.png')
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/image/image_of_people.png', 'wb') as file:
            file.write(f.read())
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return render_template('main5.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')