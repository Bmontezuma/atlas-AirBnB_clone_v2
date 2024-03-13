#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Teardown application context
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Displays a HTML page with a list of states
    """
    states = sorted(list(storage.all(State).
                    values()), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities_list(id):
    """
    Displays a HTML page with cities of a specific state
    """
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', not_found=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
