#!/usr/bin/python3
from flask import Flask

"""
This script starts a Flask web application with three routes
- '/' displays "Hello HBNB!"
- '/hbnb' displays "HBNB"
- '/c/<text>' displays "C "
"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Displays 'C ' followed by the value of the text variable (replace underscore _ symbols with a space )"""
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
