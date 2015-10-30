from peewee.peewee import *
db = SqliteDatabase('database.db')

class Concern(Model):
  #id, city_id
  title = TextField(null=True)
  body_name = CharField(null=True)
  enactment_date = DateTimeField(null=True)
  intro_date = DateTimeField(null=True)
  passed_date = DateTimeField(null=True)
  status_name = CharField(null=True)
  type_name = CharField(null=True)
  city_id = IntegerField(null=True)
  record_id = IntegerField(null=True)


  class Meta:
    database = db