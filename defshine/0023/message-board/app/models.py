from app import db
from datetime import datetime


class Message(db.Document):
    author = db.StringField(max_length=20, required=True)
    content = db.StringField(max_length=200, required=True)
    time = db.DateTimeField(default=datetime.now())

    def to_json(self):
        return {
            'author': self.author,
            'content': self.content,
            'time': self.time
        }
