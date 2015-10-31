import tkinter as tk
from tkinter import messagebox
import ttk as ttk
#from tkinter import Tk, StringVar, ttk
from city import *

CITIES = [
    "Seattle",
    "Chicago",
]

def generateReport(city):
    cityMatters = Matters(city.get(), matterListDict)
    results_0 = cityMatters.calculate(0)
    results_1 = cityMatters.calculate(1)
    (results_2_0, results_2_1) = cityMatters.calculate(2)
    
    #~ messagebox.showinfo(title="City", message="City: " + str(city.get()) + "\nCategory: " + str(cat.get()))
    tk.Label(frame, text="   ", font="Symbol 11").grid(row=3)
    
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
        #canvas.grid(row=rowNb+1, column=0, columnspan=6, sticky=tk.W)
        canvas[i].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
    notebook.grid(row=4, column=0, columnspan=4, sticky=tk.W)
    
    # First Tab    
    print('Average Time Before Meeting'),
    text = ''
    for key in sorted(results_0):
        text += key + ' : ' + str(results_0[key]) + ' days' + '\n'
        #print(text)
        #tk.Label(tab1, text=text, font="Symbol 11").grid(row=rowNb+1, column=0, columnspan=6, sticky=tk.W)
    #print(text)
    canvas_id = canvas[0].create_text(0, 10, font="Symbol 11", anchor = "nw")
    canvas[0].itemconfig(canvas_id, text=text)
    print('... Done')
    
    # Second Tab
    print('\nNumber of Files Per Body'),
    text = ''
    for key in sorted(results_1):
        text += key + ' : ' + str(results_1[key]) + '\n'
        #print(text)
        #tk.Label(tab2, text=text, font="Symbol 11").grid(row=rowNb+1, column=0, columnspan=6, sticky=tk.W)
    #print(text)
    canvas_id = canvas[1].create_text(0, 10, font="Symbol 11", anchor = "nw")
    canvas[1].itemconfig(canvas_id, text=text)
    print('... Done')
    
    # Third Tab
    print('\nStatus Per Type of File'),
    row = 10
    for key in sorted(results_2_0):
        text_header = ''
        text_body = ''
        
        # Header
        canvas_id = canvas[2].create_text(5, row, font="Symbol 11 bold", anchor = "nw")
        text_header = key + ' : ' + str(results_2_0[key]) + '\n'
        canvas[2].itemconfig(canvas_id, text=text_header)
        row += 18
        
        # Body
        key_dict = results_2_1[key]
        canvas_id = canvas[2].create_text(5, row, font="Symbol 11", anchor = "nw")
        count = 0
        for status in sorted(key_dict):
            count += 1
            text_body += '  ' + status + ' : ' + str(key_dict[status]) + '\n'
            #tk.Label(tab3, text=text_body, font="Symbol 11").grid(row=rowNb, column=0, columnspan=6, sticky=tk.W)
        canvas[2].itemconfig(canvas_id, text=text_body)
        
        row += count * 16 + 5
    print('... Done')
            
    notebook.select(tab[0])
    
# Create tkinter window
root = tk.Tk()
root.title('City Stay')
# Create tkinter frame
frame = tk.Frame(root, width=400, height=400)
frame.option_add('*Dialog.msg.font', 'Symbol 11')
frame.pack()

# Cities
labelCity = tk.Label(frame, text= " Select City:  ", font="Symbol 11").grid(row=0, column=0, sticky=tk.W)
# Create city drop list
cityName = tk.StringVar(frame)
cityName.set(CITIES[0]) # Default value
drop = tk.OptionMenu(frame, cityName, *CITIES)
drop.config(font=('Symbol',11),width=12)
drop['menu'].config(font=('Symbol',11),)
drop.grid(row=0, column=1, sticky=tk.W)


# Categories
#~ tk.Label(frame, text= "Select Category:", font="Symbol 11").grid(row=0, column=4, columnspan=2, sticky=tk.W)
#~ #Create category radio list
#~ category = tk.IntVar()
#~ category.set(0)
#~ tk.Radiobutton(frame, text = "Matter", variable=category, value=1, font="Symbol 11").grid(row=1, column=4, columnspan=2, sticky=tk.W)
#~ tk.Radiobutton(frame, text = "Event", variable=category, value=2, font="Symbol 11").grid(row=2, column=4, columnspan=2, sticky=tk.W)

# Column Separation
#tk.Label(frame, text="  ", font="Symbol 11").grid(row=0, column=2)

# Generate button
genButton = tk.Button(frame, text="Generate Report", font="Symbol 12 bold", command=lambda: generateReport(city=cityName))
genButton.grid(row=0, column=2, sticky=tk.E)

# Prevent Tkinter to resize...
tk.Label(frame, text="  ", font="Symbol 11").grid(row=0, column=3)

root.mainloop()
