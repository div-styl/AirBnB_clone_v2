#!/usr/bin/python3
"""
start a flask application
"""

from re import S
from flask import Flask, render_template
from models import *
from models import storage
from models import state
from models import amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filter():
    # Get all the states and amenities from the storage
    states = storage.all(state)
    amenities = storage.all(amenity)

    # Render the template with the states and amenities
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def tear_db(exception):
    """
    Closes the storage connection when the application context is torn down.

    Args:
        exception: The exception that caused the teardown.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
