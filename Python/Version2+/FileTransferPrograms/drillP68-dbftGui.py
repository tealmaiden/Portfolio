import os
import wx
import wx.lib.agw.multidirdialog as MDD
import time
import shutil
 
wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
 
class MyForm(wx.Frame): #frame is window
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File and Folder Dialogs Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()
 
        # create the buttons and bindings
        dirDlgBtn1 = wx.Button(panel, label="Choose Source")
        dirDlgBtn1.Bind(wx.EVT_BUTTON, self.onDir1)

        dirDlgBtn2 = wx.Button(panel, label="Choose Destination")
        dirDlgBtn2.Bind(wx.EVT_BUTTON, self.onDir2)

        moveBtn=wx.Button(panel, label="Check and Move Files")
        moveBtn.Bind(wx.EVT_BUTTON, self.moveUFiles) 
        
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
            print 'Source folder:', src    
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
            print 'Destination folder:', dst
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
                    print 'Change made to',f,'within 24 hr. File moved from Source to Destination folder.'
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
                          
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
