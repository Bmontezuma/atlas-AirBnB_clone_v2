#!/usr/bin/python3
"""
This script starts a Flask web application with specified routes.
"""

from flask import Flask, render_template
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
    """Displays 'C ' followed by the value of the text variable
       (replace underscore _ symbols with a space)"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """Displays 'Python ' followed by the value of the text variable
       (replace underscore _ symbols with a space)"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Displays an HTML page with the number if n is an integer"""
    return render_template('6-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """Displays an HTML page with the number and its odd/even status"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
