## Simple Loops

___
### Objective
* Create a starcaise with # signs.
* Create a reverse staircase with # signs and constraints.
* Create a funtion that displays integers up the the number entered.
* Call them from one file.

### Steps Taken

**Count Loop**
* Wrote a for loop that incrementally writes lines with increasing numbers signs up to the number (n) entered by the user.

**Staircase**
* Wrote a for loop that incrementally writes lines with increasing numbers of # signs up to the number (n) entered by the user.
* This displays from left to right by default as such:
```
#
##
###
```
**Reverse Staircase**
* Wrote a for loop similar to the above staircase.
* To reverse the direction of the staircase, I needed to add spaces in front of the # signs equal to n minus the number of # signs for each line:
```
  #
 ##
###
```
* To achieve this I used Enumerable.Repeat to repeat the number of spaces necessary for each line.
* To constrain the input I wrote an if/else clause.

**Calling them all from one file**
* Used the internal access modifier on each function so that they could be called from another file in the project.
* Created a file Program.cs which called the functions.

### Results
* Learned how to call functions from other classes and class files.
* Got practice on making different types of loops.
