import os
import logging

logging.basicConfig(level=logging.INFO)

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

import time

app = Flask(__name__)

class Config(object):
    DEBUG = True
    USERNAME='admin'
    PASSWORD='1234'
    DATABASE='/tmp/flaskr.db'
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY='shdjkandscbowduAIJNnjas9aSKAJSka'

# 设置一个名为 FLASKR_SETTINGS 的环境变量，指向要加载的配置文件。
# 启用静默模式告诉 Flask 在没有设置该环境变量的情况下噤声。
app.config.from_object(Config)


# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    logging.info('Connects to the specific database.')
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    g.db = rv
    logging.info(rv)
    return rv


def init_db():
    with app.app_context():
        db = connect_db()
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

@app.template_filter('format_time')
def format_time_filter(t):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))

@app.route('/')
def index():
    cur = g.db.execute('select name,title,text,created_at from entries order by id DESC ')
    entries = [dict(name=row[0], title=row[1], text=row[2], created_at=row[3]) for row in cur.fetchall()]
    logging.info(entries)
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    g.db.execute('insert into entries (name,title,text,created_at) VALUES (?,?,?,?)',
                 (request.form['name'], request.form['title'], request.form['text'], time.time()))
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.secret_key = app.config['SECRET_KEY']
    app.run()
