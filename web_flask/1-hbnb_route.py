#!/usr/bin/python3
"""Import Flask module """
from flask import Flask
""" create an instance of Flask class"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    """Displays Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """displays HBNB """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
