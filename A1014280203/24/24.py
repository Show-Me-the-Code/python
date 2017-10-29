from flask import Flask, request, render_template, redirect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DATETIME, Integer, Column
Base = declarative_base()

app = Flask(__name__)
app.secret_key = 'key'


class Post(Base):

    __tablename__ = 'todo'

    postID = Column(Integer, primary_key=True)
    postName = Column(String(50))
    createdAt = Column(DATETIME)
    content = Column(String(1500))


class DataBase(object):

    def __init__(self):
        self.info = {
            'user': '',
            'passwd': '',
            'ip': '',
            'port': '',
            'database': ''
        }
        self.session = self.make_connect()

    def __del__(self):
        if self.session:
            self.session.close()

    def make_connect(self):
        connect_str = 'mysql+pymysql://{user}:{passwd}@{ip}:{port}/{database}'.format_map(self.info)
        engine = create_engine(connect_str)
        DBSession = sessionmaker(engine)
        session = DBSession()
        return session

    def query_all_post(self):
        items = self.session.query(Post).order_by(Post.postID).all()
        if not isinstance(items, list):
            return [items]
        return items

    def add_post(self, item):
        self.session.add(item)
        self.session.commit()


@app.route('/', methods=['POST', 'GET'])
def show():
    pass


@app.route('/add', methods=['GET', 'POST'])
def add():
    pass
