#!/usr/bin/python3
"""
Starts a Flask web application.

This script starts a Flask web application that listens on 0.0.0.0, port 5000.
It retrieves data from the storage engine (FileStorage or DBStorage) using the
`storage` module from `models`.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Display a HTML page with all states.

    Retrieves all states from the storage
    and sorts them alphabetically by name.
    Then, renders an HTML template that displays each state.
    """
    states = storage.all('State').values()
    states_sorted = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=states_sorted)


@app.route('/states/<state_id>', strict_slashes=False)
def state(state_id):
    """
    Display a HTML page with cities of a specific state.

    Retrieves the state with the given ID from the storage.
    If the state is found, renders an HTML
    template that displays the state name
    and its associated cities.
    If the state is not found, returns a "Not found!"
    message.
    """
    state = storage.get('State', state_id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-state.html', state=state, cities=cities)
    else:
        return "Not found!"


@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy Session.

    Called after each request to remove the current SQLAlchemy session,
    preventing any potential memory leaks.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
