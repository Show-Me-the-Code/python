"""
    Message Board
    ~~~~~~~~~~~~~

    A simple message board application written with Flask and sqlite3.
    Since it's a small application, I have not use SQLAlchemy and wtf.

    :copyright: (c) 2015 by proteam@gmail.com.
    :license: BSD.
"""
import os
import sqlite3
from datetime import datetime
from flask import Flask, g, request, render_template, flash

app = Flask(__name__)

# configuration
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'db.sqlite3'),
    SECRET_KEY = 'secret key'
))

app.config.from_object(__name__)


def connect_db():
    """Connectts to the specific database."""
    return sqlite3.connect(app.config['DATABASE'])


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db


def init_db():
    """Initalizes the database.

    >>> from run import init_db
    >>> init_db()
    """
    with app.app_context():
        db = get_db()
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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        message  = request.form['message']
        time = datetime.now()
        if username and message:
            g.db.execute(
                'insert into message_board (username, message, time) values (?, ?, ?)',
                [username, message, time]
            )
            g.db.commit()
            flash('Your meassage was successfully posted.')
        else:
            flash('Username or message can not be blank.')
    cur = g.db.execute('select username, message, time \
             from message_board order by time desc')
    posts = [dict(username=row[0], message=row[1], time=row[2]) \
                for row in cur.fetchall()]
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    app.run(debug=True)
