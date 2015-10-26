from tkinter import *
from tkinter import messagebox
#from tkinter import Tk, StringVar, ttk
from city import *


CITIES = [
    "Seattle",
    "Denver",
    "Philadelphia"
]

def messageBox(city, cat):
    if cat.get():
        messagebox.showinfo(title="City", message="City: " + str(city.get()) + "\nCategory: " + str(cat.get()))
        Label(frame, text="   ", font="Symbol 11").grid(row=5)
        cityMatters = Matters(matterListDict)
        result = cityMatters.calculate(0)
        print(result)
        Label(frame, text=result, font="Symbol 11").grid(row=6, column=0, columnspan=6, sticky=W+E)
    else:
        messagebox.showinfo(title="Error", message="No category selected!")
    
# Create tkinter window
root = Tk()
root.title('City Stay')
# Create tkinter frame
frame = Frame(root)
frame.option_add('*Dialog.msg.font', 'Symbol 11')
frame.pack()

# Cities
labelCity = Label(frame, text= "Select City:", font="Symbol 11").grid(row=0, column=0, columnspan=2, sticky=W)
# Create city drop list
cityName = StringVar(frame)
cityName.set(CITIES[0]) # Default value
drop = OptionMenu(frame, cityName, *CITIES)
drop.config(font=('Symbol',11),width=14)
drop['menu'].config(font=('Symbol',11))
drop.grid(row=1, column=0, columnspan=2, sticky=W)

# Column Separation
Label(frame, text="   ", font="Symbol 11").grid(row=0, rowspan=3, column=3)

# Categories
Label(frame, text= "Select Category:", font="Symbol 11").grid(row=0, column=4, columnspan=2, sticky=W)
#Create category radio list
category = IntVar()
category.set(0)
Radiobutton(frame, text = "Matter", variable=category, value=1, font="Symbol 11").grid(row=1, column=4, columnspan=2, sticky=W)
Radiobutton(frame, text = "Event", variable=category, value=2, font="Symbol 11").grid(row=2, column=4, columnspan=2, sticky=W)

# Row Separation
Label(frame, text="   ", font="Symbol 11").grid(row=3)

# Generate button
genButton = Button(frame, text="Generate Report", font="Symbol 12 bold", command=lambda: messageBox(city=cityName, cat=category))
genButton.grid(row=4, column=0, columnspan=6, sticky=W+E)

root.mainloop()