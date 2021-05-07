import tkinter as tk
#or "from tkinter import *", and not add the following tk's
from tkinter import ttk 

root =tk.Tk()

entry = tk.ttk.Entry(root, width = 30)
entry.pack()

button = tk.ttk.Button(root, text = "Make File") # root is parent
button.pack()

def callback():
    _text=entry.get()

    f = open('pageGenerator.html','w')

    message = """<html>
    <head></head>
    <body><p>{x}</p></body>
    </html>""".format(x=_text)

    f.write(message)
    f.close()

    print("page generated")

button.config(command = callback)

root.mainloop()
