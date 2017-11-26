## Store Opening Time Drill
An imaginary scenario where there is a store headquartered in Portland has branches in New York and London. You want to see whether each branch is open at a given time. Store hours are 9am-9pm.
___
### Objective
* Create code that will use the current time of the Portland HQ to find out the time in the NYC & London branches, then compare that time with the branch's hours to see if they are open or closed.
* Print out if each of the two branches are open or closed.

### Steps Taken
* Imported the different available time zones using pytz so that I would know how to reference them in Python.
* Identified the time zone names for each city.
* Wrote code to identify the current time in Portland and use that to determine the current times in New York and London (H:M:S).
* Converted these times to regular times (xx:xx am/pm) to display.
* Converted current times to seconds in order to compare with opening times mathematically. Opening times were between 32400 and 75600 seconds (9am-pm).
* Wrote code to print that stores are open or closed if they are open or closed at the time the program is run.

### Results
* The program is drillp65datetime.py
* There a lot of Python tools for dealing with time information. You have to figure out which modules to import. The syntax isn't always straightforward. For instance, defining regular time looks like: "%I:%M%p".
* Also, it is possible to convert the times with a function rather than explicitly multiplying and adding as I did, but I chose to do so  because it didn't take up much more space and it more clearly expressed what was happening functionally.
