## Sum of an Array
___

### Objective

Write a program that sums over an array of integers and works in the following way:
* The array is called numbers and is of size n.
* The first line in the console accepts the integer, n, denoting the array size. 
* The console accepts input for n subsequent lines i for the user to populate the array. Each input line i defines integer numbers<sub>i</sub>.
  * 1 <= n <= 10000 
  * 1 <= numbers<sub>i</sub> <= 10000, where numbers<sub>i</sub> is element i in numbers and 0 < i < n. 
* Add exception handling for non-integer input.

### Steps Taken
* Wrote a function, sum, that sums over an array, numbers, with a foreach loop.
* In the main loop:
  * Wrote code that accepts an integer as input from the console and creates an array, vals, of size n.
  * Called sum(vals).
  * Constraints and exception handling:
    * Created a try-catch function to catch non-integer entries for n.
    * Created a while loop to constrain size of n.
    * Put a try-catch function in a for loop to check that each entry vals[i] is an integer.
    * Created an if-else function to constrain size of vals[i].
    * Created an outer while loop so that the program will repeat if an exception is caught for the first entry.
    
### Results
* The program sums over an array as described in the objective.
* The bulk of the code in the main function and entire program is for contraints and exception handling, which hinders readability, but makes the program easier to use.
* As a bonus I learned how to change the entry point that the assembly uses when there are multiple Main functions, also called the setting the starup object. When I made this program it was in a project together with the SimpleLoop program. The entry point can be set in the project's properties under startup object.
