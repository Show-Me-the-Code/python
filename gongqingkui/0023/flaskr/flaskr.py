import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,\
render_template,flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
DATABASE=os.path.join(app.root_path,'flaskr.db'),
SECRET_KEY='development key',
USERNAME='admin',
PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def hello():
    app.run()
