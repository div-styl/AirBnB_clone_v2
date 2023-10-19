#!/usr/bin/python3
"""Hello HBNB"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
