import tkinter as tk
import ttk as ttk

# Create tkinter window
root = tk.Tk()
root.title('City Stay')
# Create tkinter frame
frame = tk.Frame(root, width=400, height=400)
frame.option_add('*Dialog.msg.font', 'Symbol 11')
frame.pack()

xscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

yscrollbar = tk.Scrollbar(frame)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(frame, wrap=tk.NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.pack()

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)



#~ textcanvas = "Hello Worldddddddddddddddddddddddfdgggggggggggggggggggggggggggggggdsadrgdddddddddd\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\nHello World\nHow are you\n"
#~ canvas_id = canvas.create_text(0, 10, font="Symbol 11", anchor = "nw")
#~ canvas.itemconfig(canvas_id, text=textcanvas)

root.mainloop()
