import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import time

DATABASE = 'guestbook.db'
DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


@app.route('/')
def show_entires():
    cur = g.db.execute('select name,text,time from entries order by id desc')
    entries = [dict(name=row[0], text=row[1], time=row[2]) for row in cur.fetchall()]
    for i in entries:
        print i
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    g.db.execute('insert into entries (name, text, time) values (?, ?, ?)',
                 [request.form['name'], request.form['text'], current_time])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entires'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] is None:
            error = "Invalid username"
        else:
            session['logged_in'] = True
            session['name'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('show_entires'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entires'))



if __name__ == "__main__":
    app.run()
