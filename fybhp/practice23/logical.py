# -*- coding:utf-8 -*-
import redis
from flask import Flask,render_template,url_for,redirect
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Shell,Manager
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gudabaidemima'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Message(Form):
    name = StringField(u'姓名',validators=[Required()])
    message = TextAreaField(u'内容',validators=[Required()])
    submit = SubmitField(u'提交')

class Messages(db.Model):
    __tablename__ = 'messages'
    name = db.Column(db.String)
    message = db.Column(db.Text)
    time = db.Column(db.String,default = datetime.utcnow,primary_key = True)

@app.route('/',methods = ['GET','POST'])
def index():
    form = Message()
    messages = Messages.query.order_by(Messages.time.desc()).all()
    if form.validate_on_submit():
        message = Messages(name=form.name.data,message = form.message.data)
        db.session.add(message)
        return redirect(url_for('index'))
    return render_template('index.html',messages = messages,form = form)

if  __name__ == '__main__':
    manager.run()