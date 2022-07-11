# -*- coding: utf-8 -*-
"""
Spyder Editor

Send emails from Python: Make sure you are loggged into TankExchange email
"""

#import smtplib
import win32com.client
import pandas as pd

# change attachment for new emails:
attachment = 'U:\Documents\TankExchange\Marketing\emails\email1.html'
with open(attachment, 'r') as myfile:
   data=myfile.read()
   
#UsersExport-Tank_Exchange-.....csv 
userdf = pd.read_csv('UsersExport-Tank_Exchange-2022-07-11_19_19_22.csv', index_col=(2)) #index column is email column

#remove users who don't want to be emailed
optOutList = ["dummy1@email", "dummy2@email"]
for item in optOutList:
    userdf.drop(userdf.index[userdf.index == item], inplace = True)
    
recipientNames = userdf["Name"]
recipientList = userdf.index
outlook = win32com.client.Dispatch('outlook.application')

for recipient in recipientList:
    
    #Accessing name:
    recipientrow = userdf.loc[recipient]    
    name = recipientrow["Name"]
    if "(" in name and ")" in name: 
        index1 = name.find("(")+1
        index2 =name.find(")")
        name=name[index1:index2]
    elif "," in name:
        strindex = name.find(",")
        if name[strindex + 1]!=" ":
            strindex += 1
        else:
            strindex += 2
        name = name[strindex:]
        if " " in name:
            spaceindex = name.find(" ")
            name = name[:spaceindex]
    elif " " in name:
        spaceindex = name.find(" ")
        name = name[:spaceindex]
    print(name)
    
    msg = """
    <html>
      <head>
      </head>
      <body topmargin="0" rightmargin="0" bottommargin="0" leftmargin="0" marginwidth="0" marginheight="0" width="100%" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; width: 100%; height: 100%; -webkit-font-smoothing: antialiased; text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; line-height: 100%;
 	background-color: #ffffff;
 	color: #000000;"
 	bgcolor="#ffffff"
 	text="#000000">
          <table border="0" cellpadding="0" cellspacing="0" align="center"
 	bgcolor="#FFFFFF"
 	width="560" style="border-collapse: collapse; border-spacing: 0; padding: 0; width: inherit;
 	max-width: 560px;" class="container">
            <tr>
        		<td align="left" valign="top" style="border-collapse: collapse; border-spacing: 0; margin: 0; padding: 0; padding-left: 6.25%; padding-right: 6.25%; width: 87.5%; font-size: 17px; font-weight: 400; line-height: 160%;
         			padding-top: 25px; 
         			color: #000000;
         			font-family: sans-serif;" class="paragraph">
        				Hi {0},
        		</td>
         	</tr>
          </table>
      </body>
    </html>""".format(name)
    
       
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = 'Three important announcements' #'What\'s your \"duh\" question?'
    mail.HTMLBody = msg + data   
    mail.Send()
