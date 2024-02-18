#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ displays HBNB! """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """
    andles the '/c/<text>' path, replacing underscores with spaces
    and displaying 'C ' followed by the text
    """
    # Replace underscores with spaces in the text variable
    text_with_spaces = text.replace("_", " ")

    # Combine "C " and the text with spaces
    display_text = "C " + text_with_spaces

    return display_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
