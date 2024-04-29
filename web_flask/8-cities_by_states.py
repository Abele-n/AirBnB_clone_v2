#!/usr/bin/python3
"""
Script that starts a Flask web application.

Routes:
    /states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted by
    name (A->Z) tip
      LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
    If a State object is found with this id:
      H1 tag: “State: ”
      H3 tag: “Cities:”
      UL tag: with the list of City objects linked to the State sorted by name
      (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
      H1 tag: “Not found!”
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
"""Define the Flask application instance."""
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """Define the cities_by_states page."""
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('8-cities_by_states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    """Define the Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
