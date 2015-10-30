from peewee import *
from concern import Concern

# Events: child of Concern
class Event(Concern):
  def __init__(self):
    print("Event")
