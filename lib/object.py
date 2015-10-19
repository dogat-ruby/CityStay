import sqlite3 
import sys

# NOTE: This is a base class that acts like a database-wrapper
# There are existing database wrapper for import as well
class Object(object):
  def __init__(self):
    print("Created object of class")

  def class_name(self):
    return "Object"

  def required_keys(self):
    print("ERROR! Should be implemented in subclass!")
    return None

  def sanitize_dict(self,dictionary):
    result = []
    for d in dictionary:
      r = dict(d)
      for key,value in d.items():
        new_key = key[6:]
        if new_key in self.required_keys():
          r[new_key] = value 
        del r[key]
      result.append(r)
    return result
    
  def create(self, dictionary):
    print("ERROR! Should be implemented in subclass!")
    return None

  def find_by_id(input):
    print "TBD"
    return None

  def find_by_key(key, value):
    print "TBD"
    return None

  def find_by_keys(dictionary):
    print "TBD"
    return None    