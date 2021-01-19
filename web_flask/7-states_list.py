#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page sorted by name (A->Z)
    """
    states_all = list(storage.all("State").values())
    return (render_template('7-states_list.html', states_all=states_all))


@app.teardown_appcontext
def teardown(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
