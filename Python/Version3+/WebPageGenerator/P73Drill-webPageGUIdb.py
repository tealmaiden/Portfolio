import tkinter as tk
from tkinter import ttk 
import sqlite3

root = tk.Tk()

#Enter string for page
entry = tk.ttk.Entry(root, width = 30)
entry.pack()

#Make Page
makeButton = tk.ttk.Button(root, text = "Make File")
makeButton.pack()

#Select Old Entries
selectButton = tk.ttk.Button(root, text = "Select Previous Entries") 
selectButton.pack()

#What happens on button click to make page:
def callMakeButton():
    _text=entry.get()

    f = open('pageGenerator.html','w')

    message = """<html>
    <head></head>
    <body><p>{x}</p></body>
    </html>""".format(x=_text)

    f.write(message)
    f.close()

    print("page generated")

    ##Store Entries in Database/SQLite:
    conn = sqlite3.connect('entries.db')
    conn.execute('CREATE TABLE IF NOT EXISTS \
                entryTable(ID INTEGER PRIMARY KEY AUTOINCREMENT, theEntry TEXT)')
    conn.execute('INSERT INTO entryTable (theEntry) VALUES (?)', [_text])
    conn.commit()

def callSelectButton():
    window2 = tk.Toplevel(root)
    window2.title('Select Previous Entry')
 
    #precursor to display entries in database
    conn = sqlite3.connect('entries.db')
    cursor = conn.execute("SELECT theEntry FROM entrytable")
    words = cursor.fetchall()
    conn.commit()
    #words=[list(word) for word in words]

    makeButton2 = tk.ttk.Button(window2, text = "Make File")
    makeButton2.grid()

    global selectionList
    selectionList=[]
    
    #for loop that displays entries in labels in grid rows
    def checked(text):        
        return lambda : selectionList.append(text)

    for word in words:
        entryCheck=tk.ttk.Checkbutton(window2, text=word, command=checked(word))
        entryCheck.grid(sticky = 'nsew')

    def callMakeButton2():
        y = [i[0] for i in selectionList]
        z=(', '.join(y))

        f = open('pageGenerator.html','w')

        message = """<html>
        <head></head>
        <body><p>{x}</p></body>
        </html>""".format(x=z)

        f.write(message)
        f.close()

        print("page generated")

    makeButton2.config(command = callMakeButton2)
    window2.mainloop()
    

makeButton.config(command = callMakeButton)
selectButton.config(command = callSelectButton)

root.mainloop()

###NEW Stuff:
#store entries in database:
#create table and insert into it

##precursor to display entries in database
#    cursor = conn.execute("SELECT * from entryTable...")
#    rows = cursor.fetchall()
#    conn.commit()

##make dialogue that displays entries as selections

##get selected entries and display them in new page 
