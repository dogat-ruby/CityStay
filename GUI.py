import tkinter as tk
from tkinter import messagebox
import ttk as ttk
from peewee import *
from concern import *
from city import *
#from tkinter import Tk, StringVar, ttk

# Dictionary of city classes
citiesDict = {}

# List of cities
CITIES = [
  "Seattle",
  "Chicago",
  "Pittsburg"
]

db = SqliteDatabase('database.db', threadlocals=True)
db.connect()

# ---- Create tables ----
Matter.create_table([True])
Event.create_table([True])

# ----- Drop tables -----
# Matter.drop_table([True])
# Event.drop_table([True])

# Generate report function
def generateReport(city):
  # Debug
  print('\n>', city.get(), '\n')

  # Grabbing results
  results = []
  results = citiesDict[city.get()].updateRequest()

  # Creating notebook and canvases
  notebook = ttk.Notebook(frame)
  tab = []
  canvas = []
  for i in range(0, 3):
      tab.append(tk.Frame(notebook))
      if i == 0:
          notebook.add(tab[i], text = "Average Time Before Meeting")
      elif i == 1:
          notebook.add(tab[i], text = "Number of Files Per Body")
      elif i == 2:
          notebook.add(tab[i], text = "Status Per Type of File")
      
      canvas.append(tk.Canvas(tab[i], bg="white", width=400, height=400))
      scrollx = tk.Scrollbar(tab[i], orient=tk.HORIZONTAL, command=canvas[i].xview)
      scrollx.pack(side=tk.BOTTOM, fill=tk.X)
      scrolly = tk.Scrollbar(tab[i], orient=tk.VERTICAL, command=canvas[i].yview)
      scrolly.pack(side=tk.RIGHT, fill=tk.Y)
      canvas[i].config(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set, scrollregion=(0,0,800,800))
      canvas[i].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
  
  notebook.grid(row=3, column=0, columnspan=4, sticky=tk.W)
  
  text_offset = 10

  # First Tab    
  print('Average Time Before Meeting'),
  text = ''
  for key in sorted(results[0]):
      text += key + ' : ' + str(results[0][key]) + ' days' + '\n'
  canvas_id = canvas[0].create_text(text_offset, 10, font="Symbol 11", anchor = "nw")
  canvas[0].itemconfig(canvas_id, text=text)
  print('... Done')
  
  # Second Tab
  print('\nNumber of Files Per Body'),
  text = ''
  for key in sorted(results[1]):
      text += key + ' : ' + str(results[1][key]) + '\n'
  canvas_id = canvas[1].create_text(text_offset, 10, font="Symbol 11", anchor = "nw")
  canvas[1].itemconfig(canvas_id, text=text)
  print('... Done')
  
  # Third Tab
  print('\nStatus Per Type of File'),
  row = 10
  for key in sorted(results[2][0]):
      text_header = ''
      text_body = ''
      
      # Header
      canvas_id = canvas[2].create_text(text_offset+5, row, font="Symbol 11 bold", anchor = "nw")
      text_header = key + ' : ' + str(results[2][0][key]) + '\n'
      canvas[2].itemconfig(canvas_id, text=text_header)
      row += 18
      
      # Body
      key_dict = results[2][1][key]
      canvas_id = canvas[2].create_text(text_offset+5, row, font="Symbol 11", anchor = "nw")
      count = 0
      for status in sorted(key_dict):
          count += 1
          text_body += '  ' + status + ' : ' + str(key_dict[status]) + '\n'
      canvas[2].itemconfig(canvas_id, text=text_body)
      
      row += count * 16 + 5
  print('... Done')
          
  notebook.select(tab[0])
    
# Create tkinter window
root = tk.Tk()
root.title('City Stay')
root.resizable(0, 0)
root.minsize(width=400, height=40)
# Create tkinter frame
frame = tk.Frame(root, width=400, height=400)
frame.option_add('*Dialog.msg.font', 'Symbol 11')
frame.pack()

# Space out content from top of window
tk.Label(frame, text= "   ", font="Symbol 11").grid(row=0, column=0, sticky=tk.W+tk.E)

# Cities
labelCity = tk.Label(frame, text= " Select City:  ", font="Symbol 11").grid(row=1, column=0, sticky=tk.W)
# Create city drop list
cityName = tk.StringVar(frame)
cityName.set(CITIES[0]) # Default value
drop = tk.OptionMenu(frame, cityName, *CITIES)
drop.config(font=('Symbol',11),width=12)
drop['menu'].config(font=('Symbol',11))
drop.grid(row=1, column=1, sticky=tk.W)

# Prevent Tkinter to resize...
tk.Label(frame, text="  ", font="Symbol 11").grid(row=1, column=2)

# Generate button
genButton = tk.Button(frame, width=22, text="Generate Report", font="Symbol 12 bold", command=lambda: generateReport(city=cityName))
genButton.grid(row=1, column=3, sticky=tk.E)

# Space between user input and report tabs
tk.Label(frame, text="   ", font="Symbol 11").grid(row=2)

# Initialize classes
for item in CITIES:
  citiesDict[item] = City(item)

root.mainloop()
