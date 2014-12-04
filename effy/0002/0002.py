#!/usr/bin/env
'''

DO NOT RUN BEFORE READING THE WHOLE THING!!

Pre-request :
1. A live and running DB of your choice (Mine is Postgres for convenience)
2. A table created for storage use
3. ORM API of your choice (Mine is Sqlalchemy,to install : $ sudo pip install sqlalchemy)

ABOUT Sqlalchemy:
a. A good ref http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html
b. A dummy tutorial http://stackoverflow.com/questions/2048084/sql-alchemy-what-is-wrong
					http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html
					http://docs.sqlalchemy.org/en/rel_0_9/core/metadata.html
					http://stackoverflow.com/questions/14307238/updating-row-in-sqlalchemy-orm
'''
from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker,scoped_session
from ActivationCodeGen import codeGen

'''
Step 1: 
start a live connection with DBApi
'''
## activate echo option will print out actual SQL statement at each step.
## to connect to postgresql, create_engine('dialect://username:password@local:port/DBname')
db = create_engine('postgresql://username:password@localhost:5432/dbname', echo=True)

'''
Step 2:
Define and create table/metadata (Alternative 1), or use existing table (Alternative 2) 
'''
metadata = MetaData(db)

'''
Alternative 1: 
The following code block is of one time use, after initilization of the table 
"codes", it should be ignored and should not be run again.
'''
###########################################################
# codes = Table('codes', metadata,                          #
# 				Column('id', Integer, primary_key=True),  #
# 				Column('code', String(10), nullable=False #
# 				,unique=True)                             #
# 				)                                         #
# codes.create()                                            #
###########################################################

'''
Alternative 2:
This code block is to be used if table "codes" already
exists -- then the only work is to fetch the definition
of the table from db, like this:
'''
###################################################
codes = Table('codes', metadata, autoload=True)   #
###################################################

## this specific command flushes out all the pending request for table creation, it 
## actually create all the tables that does not exist in the db yet.
metadata.create_all(db)

'''
Step 3:
define ORM 
CAUION: STEP 3, 4, 5 CAN NOT EXCHANGE AMONGST EACH OTHER. THE SEQUENCE IS DEFINITE
'''
class Codes(object):
	__table__ = "codes"
	def __init__(self, id, code):
		self.id = id
		self.code = code
	def __repr__(self):
		return "The {0}th activation code: {1}".format(self.id, self.code)

'''
Step 4:
map between object and relational table. 
'''
mapper(Codes, codes)
metadata.create_all(db)


'''
Step 5:
Create instances of Codes class
'''

raw_codes = codeGen(200)
code_list = []
for i in range(len(raw_codes)):
	code_list.append(Codes(i+1, raw_codes[i]))


'''
Step 6:
start session. Add records and commit.
'''
sm = sessionmaker(bind=db, autocommit=False, expire_on_commit=True)
session = scoped_session(sm)
for code in code_list:
	#add will stage all the transactions
	session.add(code)

session.commit()



