# WIP: This file is to set up a database for development use

import sqlite3 
import sys


# Drop the table
con = sqlite3.connect('db/database.db')
cur = con.cursor()
cur.executescript("DROP TABLE IF EXISTS City;")
con.commit()

try:
	cur = con.cursor()
	cur.execute("CREATE TABLE Matters(Id INT, Title TEXT, BodyName STRING, EnactmentNumber STRING, EnactmentDate DATETIME, IntroDate DATETIME, PassedDate DATETIME, StatusName STRING, TypeName STRING, City STRING)")

	# Setup Cities
	cur.execute("CREATE TABLE City(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name STRING);")

	for city_name in ['Austin', 'Omaha', 'Boulder', 'Boise', 'San Francisco', 'Charlotte', 'Kansas City', 'Portland', 'Raleigh']:
		cur.execute("INSERT INTO City VALUES(NULL,?)", city_name)

	# Setup Matters

	cur.execute("INSERT INTO Matters VALUES(1, 'Matter Content 1', 'City Clerk', 'Ord 124726', EnactmentDate DATETIME, IntroDate DATETIME, PassedDate DATETIME, StatusName STRING, TypeName STRING, City STRING)")

	except sqlite3.Error, e:
	if con:
		con.rollback()
	print "Error %s:" % e.args[0]
	sys.exit(1)

	finally:
	if con:
		con.close() 


