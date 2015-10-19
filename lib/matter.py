from lib.concern import Concern
import sqlite3
import sys

# Matters: child of Concern
class Matter(Concern):
  def __init__(self):
    print("Matter")

  def required_keys(self):
    return ['Id', 'Title', 'BodyName', 'EnactmentDate', 'IntroDate', 'PassedDate', 'StatusName', 'TypeName', 'CityId']

  # TODO(DP): Refactor back out to Object class
  def create(self, dictionary):
    con = sqlite3.connect('database.sql')
    cur = con.cursor()
    #Create table if not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Matter(Id INTEGER PRIMARY KEY, Title TEXT, BodyName STRING, EnactmentDate DATETIME, IntroDate DATETIME, PassedDate DATETIME, StatusName STRING, TypeName STRING, CityId INT)")
    #Insert to DB
    for d in self.sanitize_dict(dictionary):
      print(d)
      # cur.execute("INSERT INTO Matter VALUES(NULL, 'AN ORDINANCE', 'City Clerk', '2015-03-19T00:00:00', '2015-01-26T00:00:00', '2015-03-19T00:00:00', 'Passed', 'Ordinance (Ord)', NULL);")
      cur.execute("INSERT OR REPLACE INTO Matter VALUES(?, ?, ?, ?, ?, ?, ?, ?, NULL);", (d['Id'],d['Title'], d['BodyName'], d['EnactmentDate'], d['IntroDate'], d['PassedDate'], d['StatusName'], d['TypeName']))

      con.commit()
      con.close()


r = Matter()
print(r.required_keys())

dict = [{"MatterId":1785, "MatterGuid":"843DA7B1-197B-4E3E-9496-A0A2A1FB6BBA", "MatterLastModifiedUtc":"2015-07-30T21:13:24.657", "MatterRowVersion":"AAAAAAAlFoU=", "MatterFile":"CB 118329", "MatterName":"CB 118329", "MatterTitle":"AN ORDINANCE relating to water services of Seattle Public Utilities; revising certain water rates and charges for service to wholesale customers, and amending Seattle Municipal Code Subsection 21.04.440.E in connection therewith.", "MatterTypeId":62, "MatterTypeName":"Ordinance (Ord)", "MatterStatusId":72, "MatterStatusName":"Passed", "MatterBodyId":169, "MatterBodyName":"City Clerk", "MatterIntroDate":"2015-01-26T00:00:00", "MatterAgendaDate":"2015-03-16T00:00:00", "MatterPassedDate":"2015-03-19T00:00:00", "MatterEnactmentDate":"2015-03-19T00:00:00", "MatterEnactmentNumber":"Ord 124733", "MatterRequester":"Seattle Public Utilities", "MatterNotes":None, "MatterVersion":"2", "MatterText1":None, "MatterText2":"bob.hennessey@seattle.gov", "MatterText3":None, "MatterText4":None, "MatterText5":None, "MatterDate1":None, "MatterDate2":None, "MatterEXText1":None, "MatterEXText2":None, "MatterEXText3":"No", "MatterEXText4":None, "MatterEXText5":None, "MatterEXText6":"Meg Moorehead", "MatterEXText7":None, "MatterEXText8":None, "MatterEXText9":None, "MatterEXText10":None, "MatterEXDate1":None, "MatterEXDate2":None, "MatterEXDate3":None, "MatterEXDate4":None, "MatterEXDate5":None, "MatterEXDate6":None, "MatterEXDate7":None, "MatterEXDate8":None, "MatterEXDate9":None, "MatterEXDate10":None}, {"MatterId":1786, "MatterGuid":"DD93352C-E55C-46D6-B6E4-99B68CFC5317", "MatterLastModifiedUtc":"2015-07-30T21:04:37.183", "MatterRowVersion":"AAAAAAAlFTs=", "MatterFile":"Res 31568", "MatterName":None, "MatterTitle":"A RESOLUTION establishing a 5-year budget review process and approving the proposed budget framework of the Skagit Environmental Endowment Commission for its fiscal years 2015 through 2018.", "MatterTypeId":52, "MatterTypeName":"Resolution (Res)", "MatterStatusId":95, "MatterStatusName":"Adopted", "MatterBodyId":169, "MatterBodyName":"City Clerk", "MatterIntroDate":"2015-01-26T00:00:00", "MatterAgendaDate":"2015-03-16T00:00:00", "MatterPassedDate":"2015-03-19T00:00:00", "MatterEnactmentDate":None, "MatterEnactmentNumber":None, "MatterRequester":"Seattle City Light", "MatterNotes":None, "MatterVersion":"1", "MatterText1":None, "MatterText2":"lynn.best@seattle.gov", "MatterText3":None, "MatterText4":None, "MatterText5":None, "MatterDate1":None, "MatterDate2":None, "MatterEXText1":None, "MatterEXText2":None, "MatterEXText3":None, "MatterEXText4":None, "MatterEXText5":None, "MatterEXText6":"Tony Kilduff", "MatterEXText7":None, "MatterEXText8":None, "MatterEXText9":None, "MatterEXText10":None, "MatterEXDate1":None, "MatterEXDate2":None, "MatterEXDate3":None, "MatterEXDate4":None, "MatterEXDate5":None, "MatterEXDate6":None, "MatterEXDate7":None, "MatterEXDate8":None, "MatterEXDate9":None, "MatterEXDate10":None}]
r.create(dict)
