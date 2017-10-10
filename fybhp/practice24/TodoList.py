# -*- coding:utf-8 -*-
from flask import Flask,render_template,url_for,redirect,flash,request,session
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Shell,Manager
from wtforms import StringField,SubmitField
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

class Thing(Form):
    thing = StringField(validators=[Required()])
    submit = SubmitField(u'增加事务')

class Search(Form):
    sthing = StringField(validators=[Required()])
    submit = SubmitField(u'Search')

class Things(db.Model):
    __tablename__ = 'things'
    id = db.Column(db.Integer,primary_key = True)
    thing = db.Column(db.String)
    time = db.Column(db.String,default=datetime.utcnow)

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            u = Things(thing=forgery_py.lorem_ipsum.word())
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

@app.route('/',methods = ['GET','POST'])
def index():
    form1 = Thing()
    form2 = Search()
    if form1.validate_on_submit():
        thing = Things(thing=form1.thing.data)
        db.session.add(thing)
        flash(u'任务创建成功')
        return redirect(url_for('index'))

    page = request.args.get('page',1,type=int)
    if form2.validate_on_submit():
        session['search'] = form2.sthing.data
        return redirect(url_for('.search'))
    pagination = Things.query.order_by(Things.time.desc()).paginate(\
            page,per_page=20,error_out=False)
    things = pagination.items
    return render_template('index.html',things = things,form1 = form1,form2 = form2,pagination=pagination)

@app.route('/del/<delthing>',methods = ['GET','POST'])
def delthing(delthing=None):
    if delthing != None:
        todel = Things.query.filter_by(id=delthing).first()
        db.session.delete(todel)
    return redirect(url_for('index'))

@app.route('/search/<sthing>')
def search():
    form1 = Thing()
    form2 = Search()
    page = request.args.get('page', 1, type=int)
    if form2.validate_on_submit():
        return redirect(url_for('search'))
    pagination = Things.query.filter_by(thing=session['search']).paginate( \
        page, per_page=20, error_out=False)
    things = pagination.items
    print things
    return render_template('index.html',things = things,form1 = form1,form2 = form2,pagination=pagination)

if  __name__ == '__main__':
    manager.run()