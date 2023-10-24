from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return "Добро пожаловать на главную страницу!"

# Страница формы
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f"Привет, {name}! Тебе {age} лет."
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
