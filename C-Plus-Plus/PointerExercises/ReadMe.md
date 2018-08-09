
# Pointer Exercises
I needed to code in C++ for a work project, and the concept of pointers was new to me, so I sought out to gain a better understanding partly by doing challenge questions. These are some of the challenge questions and my solutions. Solutions were posted, which helped.
___
## Objective
Complete the 3 pointer exercises from http://www.worldbestlearningcenter.com/index_files/cpp-pointer-max-exercise.htm to gain a better understanding of pointers.

1. Find the max value of a number of data values set by the user.
2. Write a C# program to accept 5 integer values from the console and print them on the screen.
3. Write a function to sort an array of ten integer values in ascending order. 

## Steps Taken
### Max Value
Made a function that loops through an array to find the max value.
Allowed the user to create the array with inputs for number of values and array values.
The array was of type int* in order to pass it to the max value function.

### Display Input
Made an array with 5 slots.
Made a pointer int* p to the array.
Allowed the user to poplulate the array by pointing to each slot in the array ( * (p+1) etc. ).

### Sort

## Results

### Max Value
Only works for integers smaller than 2,147,483,647
