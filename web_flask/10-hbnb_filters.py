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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page with Airbnb filters.

    This route handler retrieves all states, cities, and amenities from the
    storage, sorts them alphabetically by name, and renders a HTML template
    with the filters.
    """
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    cities = sorted(storage.all("City").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Remove the current SQLAlchemy Session.

    This function is called after each request to remove the current SQLAlchemy
    session, preventing any potential memory leaks.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
