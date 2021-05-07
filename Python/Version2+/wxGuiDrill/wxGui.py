import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        
        self.Centre()

        chooseOneBox=wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                           'Color Question',
                                           ['green','blue','red','yellow','orange'])

        if chooseOneBox.ShowModal()==wx.ID_OK:
            favColor=chooseOneBox.GetStringSelection()
            
        self.SetBackgroundColour(favColor)
                
        self.basicGUI()

        
    def basicGUI(self):

        #make panel:
        panel=wx.Panel(self)
        
        #namebox
        nameBox=wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'Name')
        if nameBox.ShowModal()==wx.ID_OK: #ok button
            userName=nameBox.GetValue()
        
        #yes no box
        yesNoBox=wx.MessageDialog(None, 'Do you like cats?', 'Question', wx.YES_NO)
        yesNoAnswer=yesNoBox.ShowModal()
        yesNoBox.Destroy()
        
        greeting='Hello '
        
        if yesNoAnswer==wx.ID_YES:
            greeting='Meow '

        self.SetTitle(greeting+userName+'!')
        self.Show(True)
                       
        menuBar=wx.MenuBar()
        
        fileButton=wx.Menu()
        helpButton=wx.Menu()
        attachItem=wx.Menu()
        helpItem=wx.Menu()
        sendItem=wx.Menu()

        #file options:
        sendItem=wx.MenuItem(fileButton, wx.ID_ANY, 'Send\tCtrl+S')
        fileButton.AppendItem(sendItem)

        attachItem.Append(wx.ID_ANY, 'Attach Document...')
        attachItem.Append(wx.ID_ANY, 'Attach Picture...')
        attachItem.Append(wx.ID_ANY, 'Attach Video...')
        fileButton.AppendMenu(wx.ID_ANY, 'Attach', attachItem)
    
        exitItem=wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('sad-face.png'))
        fileButton.AppendItem(exitItem)
             
        helpItem=wx.MenuItem(helpButton, wx.ID_ANY, 'About')
        helpItem.SetBitmap(wx.Bitmap('q.jpg'))
        helpButton.AppendItem(helpItem)

        menuBar.Append(fileButton, '&File') #& adds a shortkey functionality on some systems
        menuBar.Append(helpButton, 'Help')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        #toolbar:
        toolBar=self.CreateToolBar()
        quitToolButton=toolBar.AddLabelTool(wx.ID_ANY, 'Quit',
                                            wx.Bitmap('quit.jpg'))
        AttachToolButton=toolBar.AddLabelTool(wx.ID_ANY, 'Attach',
                                              wx.Bitmap('clip.jpg'))
        SendToolButton=toolBar.AddLabelTool(wx.ID_ANY, 'Send',
                                              wx.Bitmap('env.jpg'))
        toolBar.Realize() #to make it appear
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton)#to make it work
                  
        #moved add stuff to panel
        wx.TextCtrl(panel, pos=(130, 150), size=(150, 150))                        

        #add text to panel
        TextA=wx.StaticText(panel, -1, 'Enter Message', (125, 75))
        TextA.SetForegroundColour('Navy')
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
        TextA.SetFont(font)

        TextB=wx.StaticText(panel, -1, "Send Message", (125, 100))
        TextB.SetForegroundColour('White')
        TextB.SetFont(font)
              
        
    def Quit(self, e):
        self.Close()


def main():
    app=wx.App()
    windowClass(None) #can put title here too    

    app.MainLoop()

main()

