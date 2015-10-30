from peewee.peewee import *
from concern import *
from matter import *
from event import *

db = SqliteDatabase('database.db', threadlocals=True)
db.connect()
db.create_tables([Matter, Event])

first_matter = Matter.create(title='helloagain')