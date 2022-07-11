# Array A contains N cars traveling east or west, represented by 0 and 1. Count the number of pair of passing cars. If number of cars exceeds 1,000,000,000 return -1. 
# This exercise is part of a lesson on prefix sums.

#test arrays:
A = [0,1,0,1,1] #for example, pairs in this are (0,1) (0,3) (0,4) (2,3) (2,4) and the count is 5
A = [1,1,1,0,1]
A = [0,0,0,0,1]

# This took some time to understand because how to use the prefix sums was not intuitive for me. 
# It really helped to apply a few different examples.
# This answer got 100%, O(N) efficiency on first try:

def prefixSum(A):
    lengthPlus = len(A)+1
    pref = [0]*(lengthPlus)
    for i in range(1, lengthPlus, 1):
        pref[i] = pref[i-1]+A[i-1]
    return pref

#print(prefixSum(A))

def solution(A):
    count = 0
    pref = prefixSum(A)
    for i in range(len(A)):
        if A[i]==0:
            count += pref[len(A)]-pref[i+1]
            if count > 1000000000:
                return -1
    return count
  
print(solution(A))

# Here is a dummy solution I did not submit because it uses a nested for loop, which would not be efficient. 
# It was a warm up to figuring out the above solution however:
#dummy solution:
# def solution(A):
#     count = 0
#     for i in range(len(A)):
#         if A[i]==0:
#             for j in range(i, len(A), 1):
#                 if A[j]==1:
#                     count+=1
#     return count
