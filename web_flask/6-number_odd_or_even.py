#!/usr/bin/python3
'''crates a flask web application'''
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes=False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/')
def hello():
    return('Hello HBNB!')

@app.route('/hbnb')
def hbnb():
    return('HBNB')

@app.route('/c/<text>')
def c_is_fun(text):
    return('C %s' % text.replace("_", " "))

@app.route('/python', defaults={'text':'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    return('Python %s' % text.replace("_", " "))

@app.route('/number/<int:n>')
def num(n):
    return('%d is a number' % n)

@app.route('/number_template/<int:n>')
def num_tem(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def num_temp(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
