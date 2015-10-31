# coding: utf-8
import fetchDataFromAPI as API
from peewee import *
from concern import *

def sanitize_dict(dictionary):
  result = []
  for d in dictionary:
    r = dict(d)
    for key,value in d.items():
      new_key = key[6:]
      if new_key in Matter.required_keys():
        final_value = (None if value == "null" else value)
        final_key  = ("RecordId" if new_key == "Id" else new_key)
        r[final_key] = final_value
      del r[key]
    result.append(r)
  return result
  
def pushToDb(dict,city_name):
  updated_dict = sanitize_dict(dict)
  print("Pushing Data to DB: {0}".format(city_name))
  Matter.create_with_dict(updated_dict, city_name)

# Parent class
# Given that children share same methods/functions, I think it’s
# okay to declare methods here (does not have to be though), even if
# they are empty.
class City:
  def __init__(self, name):
    self.name = name
    self.list_of_dict = []
    self.fetched = False

  def parseXML(self):
    return # (list of dicts)

  def updateRequest(self):
    if not self.fetched:
      self.fetchDataFromAPI()
    else:
      self.fetchFromDb()

    results = []
    for op in range(0, 3):
      results.append(self.calculate(operation = op))
    return results

  def fetchDataFromAPI(self, category = "matters"):
    print("fetching {0}, {1}".format(self.name, category))
    self.list_of_dict = API.fetchDataFromAPI(self.name, category)
    pushToDb(self.list_of_dict, self.name)
    self.fetched = True
    return

  def fetchFromDb(self):
    self.list_of_dict = Matter.build_dict(self.name)
    return self.list_of_dict

  def calculate(self, operation):
    result = Matter.calculate(self.list_of_dict, operation)
    return result

# For testing only
# if __name__ == "__main__":
#     cityMatters = Matters(name = "chicago", dictList = matterListDict)
#     cityMatters.calculate(operation = 0)
#     cityMatters.calculate(operation = 1)
#     cityMatters.calculate(operation = 2)
#     cityMatters.fetchDataFromAPI()
#     print(cityMatters.fetched)
