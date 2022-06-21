# The prompt for this is to create a function that returns the minimum difference between the absolute value of any two sections of an array when the array is split 
# along each consecutive item. 
# For instance, if given array [3, 10, 45, 1], the function must compare the difference of 3 and 56, 13 and 46, 58 and 1 and return the one of smallest absolute value.
# The point of this exercise is to make the function efficient. My initial correct answer was not efficient, so I had to figure out what the issue was and correct it.
# The original is commented below the following final accepted answer:

# This answer got % 100 and is O(n).
def solution(A):
    mindiff = 0
    lent = len(A)
    head = 0
    tail = 0 
    total=sum(A)

    for i in range(lent-1):
        head += A[i]
        tail = total-head  
        diff = abs(head - tail)
        if i == 0:
            mindiff = diff
        if diff < mindiff:
            mindiff = diff
    return mindiff
  
  
# This was my initial draft version that returned the correct answers. Even though the code itself is more concise, it is inefficient at O(n^2), so got 53%. 
# I theorized that the repeated summations were making it take longer because it was probably increasing the number of for loops being done by the built-in python sum method:

# def solution(A):
#     mindiff = 0
#     lent = len(A)
#     #print("length: " + str(lent))

#     for i in range(lent-1):
#         head = A[0:i+1]
#         print("head: " + str(head))
#         tail = A[i+1:lent]
#         print("tail: " + str(tail))        
#         diff = abs(sum(head) - sum(tail))
#         if i == 0:
#             mindiff = diff
#         if diff < mindiff:
#             mindiff = diff
#     return mindiff
