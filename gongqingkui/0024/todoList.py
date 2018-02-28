#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,\
    render_template,flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE='/var/www/task/tasks.db',
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
    ))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
@app.route('/index.php')
def index():
    db = get_db()
    cur = db.execute('select id,status,date from tasklogs where status =1 order by id desc')
    tasklogs = cur.fetchall()
    return render_template('index.html',tasklogs=tasklogs)


@app.route('/add_task',methods=['POST'])
def add_task():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into tasklogs(content,status,date)values(?,1,?)',[request.form['content'],request.form['date']])
    db.commit()
    flash('Now TodoList was successfully posted')
    return redirect(url_for('index'))

@app.route('/confirm',methods=['GET'])
def confirm():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('update tasklogs set status = 2 where id =?',[request.args.get('id')])
    db.commit()
    flash('Now TodoList was successfully completed')
    return redirect(url_for('index'))
    
@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('index'))

def hello():
    return 'hello'

def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    
if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)
