#!/usr/bin/python3
"""
Script that starts a Flask web application.

listen on 0.0.0.0, port 5000
Route:
    /states_list: display a HTML page: (inside the tag BODY)
      H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted
    by name (A->Z) tip
      LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
"""Define the Flask application instance."""
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Define the states_list page."""
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('7-states_list.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    """Define the Flask app/request context end event listener."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
