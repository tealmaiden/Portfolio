# Count the numbers divisible by K in range A...B efficiently. This is in a prefixSums lesson.

# An obvious solution to this problem exists (dummySolution, commented below), however it is extremely slow.
# My proposed solution is extremely efficient O(1) and scores 100%. It took much  trial and error to work out the edge cases. 
# It helped to compare results with dummySolution in order to make sure the answers were correct. 
# I'm not sure how to apply prefix sums to solve this better, but this solution appears to be working well. 
# I may return to this later to understand what the intention was for this being in the prefix sums section:

import math

def solution(A, B, K):
    count = 0
    if A==0:
        count += 1
    if K>B:
        return count
    if A==B and A%K==0:
        count+=1
        return count
    elif A <= K <= B:
        count += (math.floor(B/K) - math.floor(A/K))
    elif K<A:       
        if not (A%K!=0 and B%K!=0):
            count+=1
        count += math.floor((B-A)/K)      
    return count


A = 101
B = 123
K = 5  

print("solution: " + str(solution(A, B, K)))
  
# Accurate, but extremely slow solution:
# def dummySolution(A, B, K):
#     count = 0
#     if A==0 and A==B:
#         return 1
#     elif K>B:
#         return count
#     for i in range(A, B+1, 1):
#         #print(i)
#         if i%K == 0:
#             count += 1
#     return count
#print("dummy solution: " + str(dummySolution(A, B, K)))
