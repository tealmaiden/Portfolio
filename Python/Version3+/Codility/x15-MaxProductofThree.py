# Find the max product of 3 different values in a given array. This is part of the sorting lesson.
# My initial solution was to sort the array and multiply the top 3 values. Python has an efficient built-in sort function that is O(NlogN).
# There is a tricky edge case however. You have to remember that the product of two negatives is positives.
# Here is my solution that handles the edge case of two large negative numbers.
# It is 100% O(NlogN):

def solution(A):
    A.sort()
    length = len(A)
    start = length - 3
    result = 1
    
    for i in range(start, length, 1):
        result *= A[i]

    if (A[0]<0 and A[1]<0 and A[length-1]>0):
        result2 = A[0]*A[1]*A[length-1]
        if result2 > result:
            result = result2    

    return result

A = [-3,1,2,-2,5,6]
A = [-5, 5, -5, 4]
#A = [-5, -4, -3, -2, -1]

print(solution(A))

#https://app.codility.com/demo/results/trainingNEZWGZ-3SJ/
