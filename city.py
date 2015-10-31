# coding: utf-8
import fetchDataFromAPI as API
from calculations import *
matterListDict = list_of_dict

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
			

# Matters: child of City
class Matters(City):
    def __init__(self, name, dictList):
        self.name = name
        self.list_of_dict = dictList
        #("Matters")
    def fetchDataFromAPI(self, category = "matters"):
        API.fetchDataFromAPI(self.name, category)
        self.fetched = True
        return
    def calculate(self, operation = 0):
        if operation == 0:
            # Item 1
            dictTypeNumber = get_Matter_Type_Name()
            #print('\nThe type and number of matter types are:')
            #print(dictTypeNumber)	
            dictTypeDuration = get_Matter_Intro_Agenda()
            #print('\nThe total number of days per type:')
            #print(dictTypeDuration)
            dictTypeAverageDuration = getAverageDurationPerType(dictTypeNumber, dictTypeDuration)
            #print('\n1) The average duration (in days) per type:')
            #print(dictTypeAverageDuration)
            return dictTypeAverageDuration
        elif operation == 1:
            # Item 2
            dictBodyNumber = get_Matter_Body_Name()
            #print('\n3) Number of files per body:')
            #print(dictBodyNumber)
            return dictBodyNumber
        elif operation == 2:
            # Item 3
            dictTypeNumber = get_Matter_Type_Name()
            #print('\nThe type and number of matter types are:')
            #print(dictTypeNumber)
            dictTypeStatus = get_Matter_Status()
            #print('\n2) Number of similar statuses per type of matter:')
            #print(dictTypeStatus)
            return dictTypeNumber, dictTypeStatus

# Events: child of City
class Events(City):
    def __init__(self):
        print("Events")
        
# For testing only
if __name__ == "__main__":
    cityMatters = Matters(name = "chicago", dictList = matterListDict)
    cityMatters.calculate(operation = 0)
    cityMatters.calculate(operation = 1)
    cityMatters.calculate(operation = 2)
    cityMatters.fetchDataFromAPI()
    print(cityMatters.fetched)
