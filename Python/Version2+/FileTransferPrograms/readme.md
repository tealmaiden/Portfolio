# File Transfer Programs
10-26-2016
___
## Objective
* Create a program that transfers files if they have been modified within 24 hours.
* Create another program that does the same, but with a graphical user interface where the user can select folders to choose from.
* Create another program that does the same, but displays the date and time of the last check.

## Steps Taken
* Built drillP67, which moves text files from one folder to another if they have been modified within 24 hours. The source and destination folders must be selected by editing lines in the program. It utilizes the shutil package. 
* Built drillP68dbftGui, which builds off drillP67 by including a wx GUI that allows users to select the source and destination directories with a mouse.
* Built drillP69dbftGuiDate, which builds off the above two drills by displaying the date and time of the last check in the GUI. It does this by storing the dates and times of each check in a database, using sqlite, and displaying the latest entry.

## Results
* From drillP67, I learned that, even though os package commands will display file paths with backslashes in output, when you input a file path, Python still interprets "\" as "ignore the next character", so it will truncate your path. To fix this, you can separate with two backslashes or any forward slashes.
* In the final drill, at first I tried to get the time to update immediately after a check by setting the the wx panel to refresh after clicking the check button. The panel has a command to show the last time checked from the database. This didn't work out though. Ultimately a mentor suggested just overwriting the timestamp when the button is clicked, and that worked just fine. Another reminder that there are multiple ways to do something if one way doesn't work.
