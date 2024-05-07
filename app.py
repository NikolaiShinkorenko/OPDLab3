from flask import Flask, render_template, request
import math

app = Flask(__name__)


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        a_coef = request.form.get('a_coef')
        b_coef = request.form.get('b_coef')
        c_coef = request.form.get('c_coef')

        if a_coef == "" or is_number(a_coef) is False or float(a_coef) == 0:
            return render_template('index.html', answer="некорректный коэффициент a")
        else: a = float(a_coef)
        if is_number(b_coef):
            if b_coef == "":
                b = 0
            else: b = float(b_coef)
        else: return render_template('index.html', answer="некорректный коэффициент b")
        if is_number(c_coef):
            if c_coef == "":
                c = 0
            else: c = float(c_coef)
        else: return render_template('index.html', answer="некорректный коэффициент c")

        discriminant = (b*b) - (4*a*c)
        if discriminant < 0:
            return render_template('index.html', answer="действительных корней нет")
        else:
            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)
            else:
                x1 = x2 = -b / (2*a)
            return render_template('index.html', answer=f'x₁ = {x1}, x₂ = {x2}')


if __name__ == '__main__':
    app.run(debug=True)