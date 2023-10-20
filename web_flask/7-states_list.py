#!/usr/bin/python3
"""list the states of my database"""


from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
    Route handler for displaying a list of states.

    Returns:
        A rendered HTML template with a sorted list of states.
    """

    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)

    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
