#!/usr/bin/python3
""" import flask from module"""
from flask import Flask, render_template

""" Create an instance of flask class"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """ displays Hello HNBN """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """ displays c text"""
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_is_cool(text="is cool"):
    """ display 'python', followed by value of text
    variable, default is is cool """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ displays {n} is  a number if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def display_template(n):
    """ display a html page only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
