#!/usr/bin/python3
"""list the states of my database"""


from models import *
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
app = Flask(__name__)
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
app.route("/", strict_slashes=False)


def index():
    """retunr Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """retunr HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Endpoint that returns 'C' followed by the provided
    text, with underscores replaced by spaces.

    Parameters:
        text (str): The text to be included after 'C'.

    Returns:
        str: The concatenation of 'C' and the modified text.
    """
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """
    Endpoint that returns 'Python' followed by the provided
    text, with underscores replaced by spaces.

    Args:
        text (str, optional): The text to append
            after 'Python'. Defaults to "is cool".

    Returns:
        str: The final string with 'Python' and the provided text.
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    A route that returns a string representation of the given number.

    Args:
        n (int): The number to be converted to a string.

    Returns:
        str: The string representation of the given number.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_tamplate(n):
    """
    This function handles a GET request
        to the /number_template/<int:n> endpoint.

    Parameters:
        n (int): The number specified in the URL path.

    Returns:
        str: The rendered HTML template with the number passed as a parameter.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_num(n):
    if (n % 2) == 0:
        evenness = "even"
    else:
        evenness = "odd"
    return render_template("6-number_odd_or_even.html", n=n,
                           even_or_odd=evenness)


app.route("/states_list", strict_slashes=False)


def state_list():
    """
    Route handler for displaying a list of states.

    Returns:
        A rendered HTML template with a sorted list of states.
    """
    # sorted(list(storage.all("State").values()), key=lambda x: x.name)
    states = storage.all(classes['State']).values()

    return render_template("7-states_list.html", states=states)


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
