#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /all_states: HTML page with a list of all State objects.
    /states/<state_id>: HTML page displaying the given state with <state_id>.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/all_states", strict_slashes=False)
def get_all_states():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<state_id>", strict_slashes=False)
def get_state_by_id(state_id):
    """Displays an HTML page with info about <state_id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == state_id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def remove_session(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
