# Email from Python
5-17-2022
___
## Objective
Create a Python script that can read a list of recipients from a csv file and send a personalized html-formatted email to the list using an Outlook account as the sender. 

## Steps Taken
Obtained an existing email template from this source and made adjustments: https://github.com/konsav/email-templates. This template was chosen because it is responsive and can display well on mobile.
Wrote a Python script using the pywin32 (wincom32) library. There isn't a lot of documentation on this module. The following resources were helpful:
https://www.codeforests.com/2020/06/05/how-to-send-email-from-outlook/#:~:text=How%20to%20send%20email%20from%20outlook%20in%20python,library%2C%20do%20check%20my%20other%20related%20articles%2C%20?msclkid=04c9bcded08d11ec90364a7c65054b92
https://stackoverflow.com/questions/15494911/python-win32com-outlook-attach-file-with-insert-as-text-method?msclkid=0e173e48d09911ecbfd951a858e442e9

The script sends emails using the default account you are logged into in Outlook. This particular script only works if the account you are logged into is the sender account desired. This means if you have multiple Outlook accounts, you need certain kinds of configurations. There are different ways to do this.

To personalize the message, I copied the format of the template into the Python script to use for the greeting, then attached the the html message in a way that displays as the body of the email.

## Results
I needed to change my Outlook configuration to select between different accounts on loading Outlook so that the email I am logged into could show up as the sender. This is a work script, and my company will not allow having multiple Outlook sender accounts in one Outlook instance. If this were the case, I could change the script to select between accounts.

The email came out well and looks good on mobile.
