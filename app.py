from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# 1. Санасан тоог таах
@app.route('/game1', methods=['GET', 'POST'])
def game1():
    result = ''
    if request.method == 'POST':
        number = int(request.form['number'])
        secret = int(request.form['secret'])
        if number < secret:
            result = "Их тоо оруулна уу"
        elif number > secret:
            result = "Бага тоо оруулна уу"
        else:
            result = "Баяр хүргэе! Та таалаа 🎉"
    else:
        secret = random.randint(1, 100)
    return render_template("game1_guess.html", result=result, secret=secret)

# 2. Хайч, Чулуу, Даавуу
@app.route('/game2', methods=['GET', 'POST'])
def game2():
    result = ''
    options = ['Хайч', 'Чулуу', 'Даавуу']
    if request.method == 'POST':
        player = request.form['choice']
        computer = random.choice(options)
        if player == computer:
            result = f'Тэнцсэн! Компьютер: {computer}'
        elif (player == 'Хайч' and computer == 'Даавуу') or \
             (player == 'Чулуу' and computer == 'Хайч') or \
             (player == 'Даавуу' and computer == 'Чулуу'):
            result = f'Та хожлоо! Компьютер: {computer}'
        else:
            result = f'Та хожигдлоо! Компьютер: {computer}'
    return render_template("game2_rps.html", result=result)

# 3. Зураг таах
@app.route('/game3')
def game3():
    return render_template("game3_image.html")

# 4. Фибоначчигийн таавар
@app.route('/game4', methods=['GET', 'POST'])
def game4():
    result = ''
    n = random.randint(5, 10)
    correct = fib(n)
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess == correct:
            result = 'Зөв! 🎉'
        else:
            result = f'Буруу! Зөв хариу нь {correct}'
    return render_template("game4_fibonacci.html", n=n, result=result)

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# 5. Төөрдөг байшин (HTML + JS)
@app.route('/game5')
def game5():
    return render_template("game5_maze.html")

if __name__ == '__main__':
    app.run(debug=True)
