import tkinter as tk
from tkinter import messagebox
import ttk as ttk
#from tkinter import Tk, StringVar, ttk
from city import *

CITIES = [
    "Seattle",
    "Denver",
    "Philadelphia"
]

def messageBox(city, cat):
    rowNb = 6
    
    notebook = ttk.Notebook(frame)
    tab1 = tk.Frame(notebook)
    tab2 = tk.Frame(notebook)
    tab3 = tk.Frame(notebook)
    notebook.add(tab1, text = "Average Duration Per File")
    notebook.add(tab2, text = "Status Per Type of File")
    notebook.add(tab3, text = "Number of Files Per Body")
    notebook.grid(row=rowNb, column=0, columnspan=6, sticky=tk.W)
    if cat.get():
        notebook.select(tab1)
        messagebox.showinfo(title="City", message="City: " + str(city.get()) + "\nCategory: " + str(cat.get()))
        tk.Label(frame, text="   ", font="Symbol 11").grid(row=5)
        cityMatters = Matters(matterListDict)
        results = cityMatters.calculate(0)
        
        print('From Intro to Agenda:')
        #Label(frame, text='** Average File Duration (in days) **', font="Symbol 11").grid(row=rowNb, column=0, columnspan=6, sticky=W)
    
        for key in results:
            rowNb += 1
            text = key + ' : ' + str(results[key])
            print(text)
            tk.Label(frame, text=text, font="Symbol 11").grid(row=rowNb+1, column=0, columnspan=6, sticky=tk.W)
            
    else:
        messagebox.showinfo(title="Error", message="No category selected!")
    
# Create tkinter window
root = tk.Tk()
root.title('City Stay')
# Create tkinter frame
frame = tk.Frame(root)
frame.option_add('*Dialog.msg.font', 'Symbol 11')
frame.pack()

# Cities
labelCity = tk.Label(frame, text= "Select City:", font="Symbol 11").grid(row=0, column=0, columnspan=2, sticky=tk.W)
# Create city drop list
cityName = tk.StringVar(frame)
cityName.set(CITIES[0]) # Default value
drop = tk.OptionMenu(frame, cityName, *CITIES)
drop.config(font=('Symbol',11),width=14)
drop['menu'].config(font=('Symbol',11))
drop.grid(row=1, column=0, columnspan=2, sticky=tk.W)

# Column Separation
tk.Label(frame, text="   ", font="Symbol 11").grid(row=0, rowspan=3, column=3)

# Categories
tk.Label(frame, text= "Select Category:", font="Symbol 11").grid(row=0, column=4, columnspan=2, sticky=tk.W)
#Create category radio list
category = tk.IntVar()
category.set(0)
tk.Radiobutton(frame, text = "Matter", variable=category, value=1, font="Symbol 11").grid(row=1, column=4, columnspan=2, sticky=tk.W)
tk.Radiobutton(frame, text = "Event", variable=category, value=2, font="Symbol 11").grid(row=2, column=4, columnspan=2, sticky=tk.W)

# Row Separation
tk.Label(frame, text="   ", font="Symbol 11").grid(row=3)

# Generate button
genButton = tk.Button(frame, text="Generate Report", font="Symbol 12 bold", command=lambda: messageBox(city=cityName, cat=category))
genButton.grid(row=4, column=0, columnspan=6, sticky=tk.W+tk.E)

root.mainloop()
