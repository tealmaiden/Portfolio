## Simple Registered Com Windows Application for Calling .Net from VBA
___
01-28-2025

### Background
Calling applications built in modern versions of .NET (not .NET Framework) from Microsoft Office applications is a challenge due to the need for native VBA to communicate with managed code that doesn't support it. 
There is a nuget package called Excel DNA that makes it simple to call .NET from Excel, however, it is compatible only up to .NET 6. At the time of this project, this version is out of support. .NET versions that are out of support can be restricted from being used in professional development environments.
While .NET Framework 4.8 can be used, it is much slower than the latest versions of .NET (about 20 times slower by measurement of some calculations), so not ideal when speed it a priority.
There are also inconveniences to using Excel DNA with .NET 6. Even if it was allowed, end users must download the .NET 6 runtime to use it. It is also about half the speed of .NET 9 by the same test calculations.

### Objective
Build a C# COM application using .NET 9 that can be called from external applications on Windows such as Excel.

### Steps Taken
* Used C# in Visual Studio 2022.
* Followed Microsoft documentation to build an unregistered COM application using a manifest file. This didn't work unfortunately, but is included in another directory of this portfolio.
* Followed Microsoft documentation to build a registered COM application: https://learn.microsoft.com/en-us/dotnet/core/native-interop/expose-components-to-com
  * This involved building a class library and TLB file.
  * To build the TLB file, an IDL file was created at the root of the solution and manually compiled by running "midl <desired name of tlb file>" using the Visual Studio developer command prompt.
* Building the solution generates a .dll, .comhost.dll, and other files which are included in the bin/x64/Release/net9
* Build a VBA script in an Excel Spreadsheet for calling the application from COM and included it in this above Release folder.
* Instructions for registering this application and performing a test call in the above Release folder are in the How to Use section below.

### Results
The application was able to be sucessfully called from Excel. Diagnostics were printed to the log file in C://Temp/SimpleComRegisteredLog.txt.

### How to use:
1.	Acquire/activate admin rights. 
2.	Enter “cmd” in the search bar on the Windows taskbar at the bottom of your screen.
3.	Right click Command Prompt and select “Run as administrator”
4.	Navigate to the program files in the bin/x64/Release/net9 on your computer.  If you move the location of this folder, you will need to unregister the old path and follow these steps again.) Copy the folder path in the address bar, or right click on the folder and select “Copy as Path”. 
5.	In the command prompt enter “cd <path to release folder>”.
6.	Enter the command “C:\Windows\System32\regsvr32.exe SimpleComRegisteredLibrary.comhost.dll”.
7.	In a few seconds, you should see a success message that the library has been registered. There should also be information printed to the log file mentioned in Results above.
8.	Proceed to call from Excel, by opening the "call simplecom.xlsm" file in the same directory and clicking the test button. You should see a success message. You should see more info printed to the log file.
