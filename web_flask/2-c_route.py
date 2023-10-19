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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
