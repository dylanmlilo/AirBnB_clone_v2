#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the current SQLAlchemy Session after each request """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays a HTML page with a list of all State objects
    present in DBStorage sorted by name (A->Z)
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
