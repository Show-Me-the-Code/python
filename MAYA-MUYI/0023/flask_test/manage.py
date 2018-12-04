from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_test import app
from exts import db
import pymysql
from models import User, Question

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
