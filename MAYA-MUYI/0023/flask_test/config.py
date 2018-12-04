import os
import pymysql

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:299521@127.0.0.1:3306/flask_test'
SQLALCHEMY_TRACK_MODIFICATIONS = False