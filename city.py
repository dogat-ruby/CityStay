# Parent class
# Given that children share same methods/functions, I think it’s
# okay to declare methods here (does not have to be though), even if
# they are empty.
class City:
    def __init__(self, listCities):
        self.listCities = listCities
    def fetchDataFromAPI():
        return # (XML file)
    def parseXML():
        return # (list of dicts)
    def pushToSQL():
        return #Boolean: to indicate if okay or not?
    def fetchFromSQL():
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
    def updateRequest(city, operation, bool):
        if not bool:
            xmlFile = fetchDataFromAPI(city)
            dict = parseXML(xmlFile)
            pushToSQL(dict)
        else:
            dict = fetchFromSQL(city)
            result = calculate(dict, operation)
        return result
			

# Matters: child of City
class Matters(City):
    def __init__(self):
        print("Matters")
    # Use Overriding for all the City methods

    # Events: child of City
class Events(City):
    def __init__(self):
        print("Events")
    # Use Overriding for all the City methods
