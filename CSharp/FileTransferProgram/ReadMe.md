## File Transfer Program
___
12-27-16

### Objective
Build a C# program that:
* Moves files from one folder to another if they have been modified within 24 hours.
* Has methods separate from the main method, whose functions are called from within the main method. 

### Steps Taken
* Used C# in Visual Studio 2015 and the System.IO namespace.
* Made a method that moves files if changed within 24 h.
* Made methods that ask for source and destination directories.

### Results
* The program was successful, and I better understand the use of static, void, and calling methods.
* Until I noticed the second objective, I had the "move" method within the main method, so I brought that out and called it from the main method.
* I built get-directory methods to give more functionality and so that I would have more methods to call within the main method.
* The default directories are hard-coded and new entries are not remembered, so you have to enter your own default directories when using this script.
* In order to for the program to remember past entries, it would need a database such as SQLite or LocalDB. Adding one would be a good exercise in the future.
* I have not explored SQLite with C#, but I have built a more detailed [move-files program with Python] that applied SQLite and other tools.

[move-files program with Python]: https://github.com/rebeccapizano/Portfolio/tree/master/Python/Version27/DbFileTransferGuiDate
