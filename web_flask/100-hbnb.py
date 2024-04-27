#!/usr/bin/python3
"""
script that starts a Flask web application

listen on 0.0.0.0, port 5000
Routes:
    /hbnb: display a HTML page like 8-index.html, done during the 0x01. AirBnB
    clone - Web static project
      Copy files 3-footer.css, 3-header.css, 4-common.css, 6-filters.css and
      8-places.css from web_static/styles/ to folder web_flask/static/styles
      Copy all files from web_static/images/ to folder web_flask/static/images
      Update .popover class in 6-filters.css to enable scrolling in the popover
      and set max height to 300 pixels.
      Update 8-places.css to always have the price by night on the top right
      of each place element, and the name correctly aligned and visible
      Use 8-index.html content as source code for the template 100-hbnb.html:
      Replace the content of the H4 tag under each filter title
      (H3 States and H3 Amenities) by &nbsp;
      Make sure all HTML tags from objects are correctly used
      (example: <BR /> must generate a new line)
      State, City, Amenity and Place objects must be loaded from DBStorage and
      sorted by name (A->Z)
"""

from flask import Flask, render_template, Markup

from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    all_states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    all_states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    places.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    ctxt = {
        'states': all_states,
        'amenities': amenities,
        'places': places
    }
    return render_template('100-hbnb.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
