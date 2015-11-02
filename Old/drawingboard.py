xscrollbar = Scrollbar(master, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)

yscrollbar = Scrollbar(master)
yscrollbar.pack(side=RIGHT, fill=Y)

text = Text(master, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.pack()

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)