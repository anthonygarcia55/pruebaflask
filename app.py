from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sumar', methods=['POST'])
def sumar():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    suma = num1 + num2
    return render_template('resultado.html', suma=suma)

if __name__ == '__main__':
    app.run(debug=True)