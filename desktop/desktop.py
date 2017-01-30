# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'desktop.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('DESKTOP_SETTINGS', silent=True)


# DB Connections
def get_db():
    """Opens a new DB connection, checks if one exists"""
    """
    if not hasattr(g, 'dbconnect_db'):
        g.dbconnect = connect_db()
    return g.dbconnect
        """
    pass

@app.teardown_appcontext
def close_db(error):
    """closes the db again at end of the request. """
    """
    if hasattr(g, 'dbconnect_db'):
        g.dbconnect.close()

    """
    pass

def connect_db():
    pass