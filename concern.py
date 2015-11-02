import sqlite3
import re
import datetime
from peewee import *
from calculations import *
from termcolor import colored

db = SqliteDatabase('database.db')

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

  def required_keys():
    return ['Id', 'Title', 'BodyName', 'EnactmentDate', 'IntroDate', 'AgendaDate', 'PassedDate', 'StatusName', 'TypeName']

  def create_with_dict(dict, city_name):
    skip_count = 0
    # Another way to mass insert is Model.create(*dict)
    print(colored("- Importing {0} records".format(len(dict)),'green'))
    for record in dict:
      id = int(record['RecordId'])
      if Matter.select().where(Matter.record_id == id, Matter.city_name == city_name ).count() > 0:
        skip_count +=1
        continue
        
      Matter.insert(
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
      ).execute()

    print(colored("  > Skipped #{0} records".format(skip_count), 'magenta'))

  def build_dict(city_name):
    dict = []
    print("CityName: " + city_name)
    print("Record Count: {0}".format(Matter.select().where(Matter.city_name == city_name).count()))
    for record in Matter.select().where(Matter.city_name == city_name):
      dict.append({
        'MatterId' : record.record_id,
        'MatterTitle': record.title,
        'MatterBodyName': record.body_name,
        'MaterEnactmentDate': record.enactment_date,
        'MatterIntroDate': record.intro_date,
        'MatterPassedDate': record.passed_date,
        'MatterAgendaDate': record.agenda_date,
        'MatterStatusName': record.status_name,
        'MatterTypeName': record.type_name,
        'MatterCityName': record.city_name
      })
    # print(dict)  
    return dict

  def calculate(list_of_dict, operation = 0):
    if operation == 0:
      # Item 1
      dictTypeNumber = get_Matter_Type_Name(list_of_dict)
      #print('\nThe type and number of matter types are:')
      #print(dictTypeNumber)  
      dictTypeDuration = get_Matter_Intro_Agenda(list_of_dict)
      #print('\nThe total number of days per type:')
      #print(dictTypeDuration)
      dictTypeAverageDuration = getAverageDurationPerType(dictTypeNumber, dictTypeDuration)
      #print('\n1) The average duration (in days) per type:')
      #print(dictTypeAverageDuration)
      return dictTypeAverageDuration
    elif operation == 1:
      # Item 2
      dictBodyNumber = get_Matter_Body_Name(list_of_dict)
      #print('\n3) Number of files per body:')
      #print(dictBodyNumber)
      return dictBodyNumber
    elif operation == 2:
      # Item 3
      dictTypeNumber = get_Matter_Type_Name(list_of_dict)
      #print('\nThe type and number of matter types are:')
      #print(dictTypeNumber)
      dictTypeStatus = get_Matter_Status(list_of_dict)
      #print('\n2) Number of similar statuses per type of matter:')
      #print(dictTypeStatus)
      return dictTypeNumber, dictTypeStatus

class Event(Concern):
  def nothing():
    return None
