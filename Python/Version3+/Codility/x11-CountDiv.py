#Count the numbers divisible by K in rang A..B efficiently. This is in a prefixSums lesson.

# A work in progress. This solution is efficient O(1), but give a wrong answer on one of the last checks. It scores 87%. Needs improvement. 
# Not sure how to apply prefix sums to solve this better, but this solution appears to be close to working well:

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
  
# Accurate, but slow solution:
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
