#!/usr/bin/python3
"""list the states of my database"""


from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a list of states and render it as an HTML template.

    Returns:
        The rendered HTML template with a sorted list of states.
    """

    # Get all the state objects from the storage
    states = storage.all("State").values()

    # Render the HTML template with the states
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tear_db(exception):
    """
    Teardown function to close the database connection.

    Args:
        exception (Exception): The exception raised, if any.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
