# coding: utf-8
from calculations import *

# Parent class
# Given that children share same methods/functions, I think it’s
# okay to declare methods here (does not have to be though), even if
# they are empty.
class City:
  def __init__(self, name):
    self.name = name
    self.fetched = False
  def fetchDataFromAPI(self):
    return # (XML file)
  def parseXML(self):
    return # (list of dicts)
  def pushToSQL(self):
    return #Boolean: to indicate if okay or not?
  def fetchFromSQL(self):
    return # (list of dicts)
  def calculate(self):
    return
  def updateRequest(city_name, operation):
    self.name = city_name
    if not self.fetched:
      xmlFile = fetchDataFromAPI(city)
      dict = parseXML(xmlFile)
      city.create(dict)
    else:
      dict = fetchFromSQL(city)
      result = calculate(dict, operation)
    self.fetched = True
    return result
    