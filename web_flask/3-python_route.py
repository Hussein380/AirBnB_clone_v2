#!/usr/bin/python3
""" import flask from module"""
from flask import Flask

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """displays ''Python followed by value of text variable """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
