from lib.object import Object

# Parent class
# Given that children share same methods/functions, I think it’s
# okay to declare methods here (does not have to be though), even if
# they are empty.
class City:
    def __init__(self, name):
        self.name = name
        self.fetched = False
    def fetchDataFromAPI():
        return # (XML file)
    def parseXML(self):
        return # (list of dicts)
    def pushToSQL(self):
        return #Boolean: to indicate if okay or not?
    def fetchFromSQL(self):
        return # (list of dicts)
    def calculate(dict, operation):
        result = 0
        if operation == "mean":
            key = 0
            for item in dict:
                result = result + dict[item][key]
        elif operation == "max":
            print("Max")
        elif operation == "count":
            print("Count")
        return result #(result of operation: mean, max, count, etc)
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