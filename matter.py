from peewee.peewee import *
import sqlite3
import sys
import os
import re
import datetime
from concern import Concern


# Matters: child of Concern
class Matter(Concern):
  # def __init__(self, dictList=[]):
  #   self.list_of_dict = dictList
  #   print("Matter")

  def required_keys():
    return ['Id', 'Title', 'BodyName', 'EnactmentDate', 'IntroDate', 'AgendaDate', 'PassedDate', 'StatusName', 'TypeName', 'CityId']

  def create_with_dict(dict, city_id):
    for record in dict:
      if Matter.select().where(Matter.record_id == record['RecordId']).count() > 0:
        print("Skipping: Record #{0} exist".format(record['RecordId']))
        continue

      Matter.create(
        record_id = record['RecordId'],
        title = record['Title'],
        body_name = record['BodyName'],
        enactment_date = record['EnactmentDate'],
        intro_date = record['IntroDate'],
        passed_date = record['PassedDate'],
        status_name = record['StatusName'],
        type_name = record['TypeName'],
        city_id = city_id
      )

  def calculate(self, operation = 0):
    if operation == 0:
      MatterIntroDate = [d['MatterIntroDate'] for d in self.list_of_dict if d['MatterIntroDate']]
      #print("MatterIntroDate = ", MatterIntroDate)  
      for index in range (len(MatterIntroDate)):
        date = re.split('T', MatterIntroDate[index])
        MatterIntroDate[index] = date[0]
      #print("New MatterIntroDate = ", MatterIntroDate)
      print('length of MatterIntroDate = ',len(MatterIntroDate))

      ##MatterAgendaDate
      MatterAgendaDate = [d['MatterAgendaDate'] for d in self.list_of_dict if d['MatterAgendaDate']]
      #print("MatterAgendaDate = ",MatterAgendaDate)
      for index in range (len(MatterAgendaDate)):
        date = re.split('T', MatterAgendaDate[index])
        MatterAgendaDate[index] = date[0]
      #print("New MatterIntroDate = ", MatterAgendaDate)
      print('length of MatterAgendaDate = ',len(MatterAgendaDate))
      array_len = len(MatterAgendaDate)

      total = 0
      for index in range (array_len):
        try:
          date1 = MatterAgendaDate[index]
        except IndexError:
          print("element not present MatterAgendaDate at index = ",index)
        try:
          date1 = MatterIntroDate[index]
        except IndexError:
          print("element not present MatterIntroDate at index = ",index)

        date = MatterIntroDate[index]
        if(re.search(r'null',date)):
            continue  
        (y1, m1, d1) = date.split('-')
        date = MatterAgendaDate[index]
        #print('date2 = ',date)
        if(re.search(r'null',date)):
            continue
        (y2, m2, d2) = date.split('-')
        (y1, m1, d1, y2, m2, d2) = int(y1), int(m1), int(d1), int(y2), int(m2), int(d2)
        d1 = datetime.date(y1, m1, d1)
        d2 = datetime.date(y2, m2, d2)
        delta = d2 - d1
        print('Diff between Matter Intro date and Matter Agenda date = ',delta.days)
        # Adding to total
        total = total + delta.days

      total_days = total / len(MatterAgendaDate)
      total_days_int = int(total / len(MatterAgendaDate))
      total_hours = int((total_days - total_days_int) * 24)
      result = 'Average: ' + str(total_days_int) + ' days and ' + str(total_hours) + ' hours'
      print(result)
      return result


# r = Matter()
# print(r.required_keys())

# dict = [{"MatterId":1785, "MatterGuid":"843DA7B1-197B-4E3E-9496-A0A2A1FB6BBA", "MatterLastModifiedUtc":"2015-07-30T21:13:24.657", "MatterRowVersion":"AAAAAAAlFoU=", "MatterFile":"CB 118329", "MatterName":"CB 118329", "MatterTitle":"AN ORDINANCE relating to water services of Seattle Public Utilities; revising certain water rates and charges for service to wholesale customers, and amending Seattle Municipal Code Subsection 21.04.440.E in connection therewith.", "MatterTypeId":62, "MatterTypeName":"Ordinance (Ord)", "MatterStatusId":72, "MatterStatusName":"Passed", "MatterBodyId":169, "MatterBodyName":"City Clerk", "MatterIntroDate":"2015-01-26T00:00:00", "MatterAgendaDate":"2015-03-16T00:00:00", "MatterPassedDate":"2015-03-19T00:00:00", "MatterEnactmentDate":"2015-03-19T00:00:00", "MatterEnactmentNumber":"Ord 124733", "MatterRequester":"Seattle Public Utilities", "MatterNotes":None, "MatterVersion":"2", "MatterText1":None, "MatterText2":"bob.hennessey@seattle.gov", "MatterText3":None, "MatterText4":None, "MatterText5":None, "MatterDate1":None, "MatterDate2":None, "MatterEXText1":None, "MatterEXText2":None, "MatterEXText3":"No", "MatterEXText4":None, "MatterEXText5":None, "MatterEXText6":"Meg Moorehead", "MatterEXText7":None, "MatterEXText8":None, "MatterEXText9":None, "MatterEXText10":None, "MatterEXDate1":None, "MatterEXDate2":None, "MatterEXDate3":None, "MatterEXDate4":None, "MatterEXDate5":None, "MatterEXDate6":None, "MatterEXDate7":None, "MatterEXDate8":None, "MatterEXDate9":None, "MatterEXDate10":None}, {"MatterId":1786, "MatterGuid":"DD93352C-E55C-46D6-B6E4-99B68CFC5317", "MatterLastModifiedUtc":"2015-07-30T21:04:37.183", "MatterRowVersion":"AAAAAAAlFTs=", "MatterFile":"Res 31568", "MatterName":None, "MatterTitle":"A RESOLUTION establishing a 5-year budget review process and approving the proposed budget framework of the Skagit Environmental Endowment Commission for its fiscal years 2015 through 2018.", "MatterTypeId":52, "MatterTypeName":"Resolution (Res)", "MatterStatusId":95, "MatterStatusName":"Adopted", "MatterBodyId":169, "MatterBodyName":"City Clerk", "MatterIntroDate":"2015-01-26T00:00:00", "MatterAgendaDate":"2015-03-16T00:00:00", "MatterPassedDate":"2015-03-19T00:00:00", "MatterEnactmentDate":None, "MatterEnactmentNumber":None, "MatterRequester":"Seattle City Light", "MatterNotes":None, "MatterVersion":"1", "MatterText1":None, "MatterText2":"lynn.best@seattle.gov", "MatterText3":None, "MatterText4":None, "MatterText5":None, "MatterDate1":None, "MatterDate2":None, "MatterEXText1":None, "MatterEXText2":None, "MatterEXText3":None, "MatterEXText4":None, "MatterEXText5":None, "MatterEXText6":"Tony Kilduff", "MatterEXText7":None, "MatterEXText8":None, "MatterEXText9":None, "MatterEXText10":None, "MatterEXDate1":None, "MatterEXDate2":None, "MatterEXDate3":None, "MatterEXDate4":None, "MatterEXDate5":None, "MatterEXDate6":None, "MatterEXDate7":None, "MatterEXDate8":None, "MatterEXDate9":None, "MatterEXDate10":None}]
# r.create(dict)
