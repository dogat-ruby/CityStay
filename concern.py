import sqlite3
import re
import datetime
from peewee.peewee import *
from calculations import *

db = SqliteDatabase('database.db')
global list_of_dict

class Concern(Model):
  #id, city_id
  title = TextField(null=True)
  body_name = CharField(null=True)
  enactment_date = DateTimeField(null=True)
  intro_date = DateTimeField(null=True)
  passed_date = DateTimeField(null=True)
  agenda_date = DateTimeField(null=True)
  status_name = CharField(null=True)
  type_name = CharField(null=True)
  city_name = CharField(null=True)
  record_id = IntegerField(null=True)

  class Meta:
    database = db

# Matters: child of Concern
class Matter(Concern):
  def __init__(self):
    super(Matter, self).__init__()
    self.list_of_dict = []

  def required_keys():
    return ['Id', 'Title', 'BodyName', 'EnactmentDate', 'IntroDate', 'AgendaDate', 'PassedDate', 'StatusName', 'TypeName']

  def create_with_dict(dict, city_name):
    skip_count = 0
    # Another way to mass insert is Model.create(*dict)
    print("- Importing {0} records".format(len(dict)))
    for record in dict:
      id = int(record['RecordId'])
      if Matter.select().where(Matter.record_id == id).count() > 0:
        skip_count +=1
        continue

      Matter.create(
        record_id = id,
        title = record['Title'],
        body_name = record['BodyName'],
        enactment_date = record['EnactmentDate'],
        intro_date = record['IntroDate'],
        passed_date = record['PassedDate'],
        agenda_date = record['AgendaDate'],
        status_name = record['StatusName'],
        type_name = record['TypeName'],
        city_name = city_name
      )
    print("  > Skipped #{0} records".format(skip_count))

  def build_dict(self, city_name):
    dict = []
    print("CityName: " + city_name)
    print("Record Count: {0}".format(Matter.select().where(Matter.city_name == city_name).count()))
    for record in Matter.select().where(Matter.city_name == city_name):
      dict.append({
        'MatterId' : record.record_id or 'null',
        'MatterTitle': record.title or 'null',
        'MatterBodyName': record.body_name or 'null',
        'MaterEnactmentDate': record.enactment_date or 'null',
        'MatterIntroDate': record.intro_date or 'null',
        'MatterPassedDate': record.passed_date or 'null',
        'MatterAgendaDate': record.agenda_date or 'null',
        'MatterStatusName': record.status_name or 'null',
        'MatterTypeName': record.type_name or 'null',
        'MatterCityName': record.city_name or 'null'
      })
    print(dict)  
    self.list_of_dict = dict
    self.save()

  def fetchDataFromAPI(self, category = "matters"):
    API.fetchDataFromAPI(self.name, category)
    self.fetched = True
    return

  def calculate(self, operation = 0):
    if operation == 0:
      # Item 1
      dictTypeNumber = get_Matter_Type_Name(self.list_of_dict)
      #print('\nThe type and number of matter types are:')
      #print(dictTypeNumber)  
      dictTypeDuration = get_Matter_Intro_Agenda(self.list_of_dict)
      #print('\nThe total number of days per type:')
      #print(dictTypeDuration)
      dictTypeAverageDuration = getAverageDurationPerType(dictTypeNumber, dictTypeDuration)
      print('\n1) The average duration (in days) per type:')
      print(dictTypeAverageDuration)
      return dictTypeAverageDuration
    elif operation == 1:
      # Item 2
      dictBodyNumber = get_Matter_Body_Name(self.list_of_dict)
      #print('\n3) Number of files per body:')
      #print(dictBodyNumber)
      return dictBodyNumber
    elif operation == 2:
      # Item 3
      dictTypeNumber = get_Matter_Type_Name(self.list_of_dict)
      #print('\nThe type and number of matter types are:')
      #print(dictTypeNumber)
      dictTypeStatus = get_Matter_Status(self.list_of_dict)
      #print('\n2) Number of similar statuses per type of matter:')
      #print(dictTypeStatus)
      return dictTypeNumber, dictTypeStatus

class Event(Concern):
  def nothing():
    return None
