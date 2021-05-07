import os
import wx
import wx.lib.agw.multidirdialog as MDD
import time
import shutil
import sqlite3
import datetime
from datetime import datetime

#?
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"

##- create a database and a table 
##- modify your script to both record date/time of 'file check' runs and 
##  to retrieve that data for use in the 'file check' process, and 
##- modify the UI to display the last 'file check' date/time 

class MyForm(wx.Frame): #the window, where you put buttons and things
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File and Folder Dialogs Tutorial")
        global panel
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()
 
        # create the buttons and bindings
        dirDlgBtn1 = wx.Button(panel, label="Choose Source")
        dirDlgBtn1.Bind(wx.EVT_BUTTON, self.onDir1)

        dirDlgBtn2 = wx.Button(panel, label="Choose Destination")
        dirDlgBtn2.Bind(wx.EVT_BUTTON, self.onDir2)

        moveBtn=wx.Button(panel, label="Check and Move Files")
        moveBtn.Bind(wx.EVT_BUTTON, self.moveUFiles) 
        #moveBtn.Bind(wx.EVT_BUTTON, panel.Update) 
        
        #SQLite
        conn = sqlite3.connect('checkTimes.db')
        conn.execute('CREATE TABLE if not exists \
                    Checks(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    checkTime DATETIME)')
        cursor = conn.execute("SELECT checkTime from Checks \
                    where oid = (SELECT max(oid) from Checks)")
        rows = cursor.fetchall()
        conn.commit()
        
        #Show Last Time Checked
        timestr=str(rows).replace("[(u'", '').replace("',)]", '')
        TextA=wx.StaticText(panel, -1, 'Last checked: '+timestr, (100, 175))
        TextA.SetForegroundColour('Navy')
        font = wx.Font(8, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        #TextA.SetFont(font)
        
        # put the buttons in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(dirDlgBtn1, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(dirDlgBtn2, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(moveBtn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        
    def onDir1(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            global src
            src=dlg.GetPath()
            print('Source folder:', src)
        dlg.Destroy()

    def onDir2(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg2 = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg2.ShowModal() == wx.ID_OK:
            global dst
            dst=dlg2.GetPath()
            print('Destination folder:', dst)
        dlg2.Destroy()

    def moveUFiles(self, event): 
        count = 0   #num files moved
        a = ('\n*************************( Check Complete )*************************')  #new line w/ string 
        b = ('********************************************************************')
        for f in os.listdir(src):
            if f.endswith(".txt"):
                srcPath = (os.path.join(src, f))    #path = source + file
                dstPath = (os.path.join(dst, f))
                mtime = (os.path.getmtime(srcPath)) #seconds from the epoch when file was modified
                now = time.time()                   #seconds from the epoch currently
                diff = now - mtime
                if diff <= 86400:                   #move if mod happened < 86400s ago
                    shutil.move(srcPath, dstPath)   #add source dir to filename
                    print('Change made to',f,'within 24 hr. File moved from Source to Destination folder.')
                    count = count + 1 
        if (count > 1):
            print(a)
            print("{} files have been moved into the destination directory".format(count))
            print(b)
        elif (count == 1):
            print(a)
            print("1 file has been moved into the destination directory") #file singular
            print(b)
        else:
            print(a)
            print("No files need to be moved at this time.")
            print(b)

        #SQLite
        conn = sqlite3.connect('checkTimes.db')
        conn.execute('CREATE TABLE if not exists \
                    Checks(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    checkTime DATETIME)')
        conn.execute('insert into Checks (checkTime) Values (datetime("now", "localtime"))')
        #cursor = conn.execute("SELECT * from Checks where oid = (SELECT max(oid) from Checks)")
        #rows = cursor.fetchall()
        conn.commit()
        refresh = datetime.fromtimestamp(now).strftime('%m/%d/%Y %H:%M:%S') 
        conn.commit()
        Text=wx.StaticText(panel, -1, 'Last checked: '+ refresh, (100, 175))
                                
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
