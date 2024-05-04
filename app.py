from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        a = int(request.form.get('a_coef'))
        b = int(request.form.get('b_coef'))
        c = int(request.form.get('c_coef'))
        discriminant = (b*b) - (4*a*c)
        if discriminant < 0:
            return render_template('index.html', answer="Действительных корней нет")
        else:
            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)
            else:
                x1 = x2 = -b / (2*a)
            return render_template('index.html', answer=f'x1 = {x1}, x2 = {x2}')


if __name__ == '__main__':
    app.run(debug=True)