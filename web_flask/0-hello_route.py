#!/usr/bin/python3
"""
    Start Flask application
"""
from flask import Flask

""" Create a Flask application instance"""
app = Flask(__name__)

""" Define a route for the root URL ('/') with t
    he option strict_slashes=False """


@app.route('/', strict_slashes=False)
def handle_requests():
    """ Define a function to handle requests to the defined route """
    return "Hello HBNB!"


if __name__ == '__main__':
    """ start te Flask development server"""
    app.run(host='0.0.0.0', port=5000)
