import base64
import re
from sqlalchemy import Column, String, DATE, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

database_info = {
    'user': '',
    'passwd': '',
    'ip': '',
    'port': '',
    'database': ''
}


class Coupon(Base):
    __tablename__ = 'coupon'

    id = Column(String(200), primary_key=True)
    deadline = Column(DATE)
    userID = Column(String(200))
    code = Column(String(200))


def make_connect(DB_info):
    connect_str = 'mysql+pymysql://{user}:{passwd}@{ip}:{port}/{database}'.format_map(DB_info)
    engine = create_engine(connect_str)
    DBSession = sessionmaker(engine)
    session = DBSession()
    return session


def parse_coupon(c_code):
    return base64.urlsafe_b64decode(c_code.encode('utf-8'))


def upload_to_database():
    session = make_connect(database_info)
    with open('coupon.txt', 'r') as file:
        for line in file.readlines():
            c_id = re.findall(r'.*/.*:(.*)\'', str(parse_coupon(line)))
            session.add(Coupon(id=c_id.pop(), code=line))
        session.commit()
        session.close()

if __name__ == '__main__':
    upload_to_database()
