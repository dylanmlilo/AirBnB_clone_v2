#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
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
def display_C_text(text):
    """
    andles the '/c/<text>' path, replacing underscores with spaces
    and displaying 'C ' followed by the text
    """
    # Replace underscores with spaces in the text variable
    text_with_spaces = text.replace("_", " ")

    # Combine "C " and the text with spaces
    display_text = "C " + text_with_spaces

    return display_text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py_text(text="is cool"):
    """
    Handles the '/python/<text>' path, replacing underscores with spaces
    and displaying 'Python ' followed by the text with "is cool" as the default
    text
    """
    # Replace underscores with spaces in the text variable
    text_with_spaces = text.replace("_", " ")

    # Combine "Python " and the text with spaces
    display_text = "Python " + text_with_spaces

    return display_text


@app.route("/number/<int:n>", strict_slashes=False)
def check_number(n):
    """ check if n is a number or not """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def pass_number_to_template(n):
    """
    check if n is a number or not
    and pass it to an html template to be rendered
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    check if n is a number or not
    and pass it to an html template to be rendered
    as an odd or even number
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
