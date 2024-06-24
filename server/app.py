#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_text(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    return '\n'.join(str(i) for i in range(number)) + '\n'

@app.route('/math/<int:a>/<operation>/<int:b>')
def math(a, operation, b):
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == 'div':
        result = a / b
    elif operation == '%':
        result = a % b
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
