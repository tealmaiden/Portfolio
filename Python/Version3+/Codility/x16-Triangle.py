# Return 1 if an array contains a set of 3 values that are triangular. Return 0 if not. This is in the sorting section.
# Triangular values are at positions P, Q, and R where 
# A[P] + A[Q] > A[R]
# A[Q] + A[R] > A[P]
# A[R] + A[P] > A[Q]

# My first solution gave the correct answer but was O^3 efficiency because the triple nested loop makes many comparisons. 
# I do not see a way to do this without the loops, but I have built in ways to get to the solution faster by rearranging the array and doing various checks.
# One thing that was apparent early on is that if a set of values is triangular, it doesn't matter the positions they are in the array.
# This means the values can be arranged in different ways.
# After some experimenting, I found that rearranging the list in a certain out-of-order way sped it up in some cases because it allowed for fewer comparisons before returning an answer.
# This sped up my original answer a little bit and raised my score about 6%.
# I also observed there can be no triangular arrays if all the values are negative, which made them easier to filter out. 
# This fixed the remaining performance issues interestingyly.

# Here is my 100% solution O(NlogN):

def isTriangle(A, P, Q, R):
    if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[P] + A[R] > A[Q]:
        return True
    else:
        return False

def trianglesort(A):
    length = len(A)
    B = [0] * length
    for i in range(length):
        if i%2 == 0:
            B[int(length-1-i/2)]=A[i]
        elif (i+1)%2 == 0:
            B[int((i+1)/2-1)] = A[i]
    return B

def solution(A):
    length = len(A)
    if length < 3:
        return 0
    A.sort(reverse=True)
    if A[0] <= 0:
        return 0
    A = trianglesort(A)
    P = 0
    while P <= length-3:
        for Q in range(P+1, length, 1):
            for R in range(Q+1, length, 1):
                if isTriangle(A, P, Q, R):
                    return 1
        P += 1
        continue
    return 0

#A = [10, 2, 5, 1, 8, 20]
A = [10, 50, 5, 1]

print(solution(A))

#Here is the solution I use to track the number of comparisons being made before finding an answer:
#def solution(A):
#    length = len(A)
#    if length < 3:
#        return 0
#    A.sort(reverse=True)
#    if A[0] <= 0:
#        return 0
#    A = trianglesort(A)
#    P = 0
#    compare = 0
#    while P <= length-3:
#        for Q in range(P+1, length, 1):
#            for R in range(Q+1, length, 1):
#                compare += 1
#                if isTriangle(A, P, Q, R):
#                    return 1, compare
#        P += 1
#        continue
#    return 0, compare

# Progression:
# https://app.codility.com/demo/results/trainingGWNNZ9-92K/
# https://app.codility.com/demo/results/trainingV3J7PX-YZJ/
# https://app.codility.com/demo/results/trainingH37Q39-EUH/
# https://app.codility.com/demo/results/training5N2VFZ-UWR/
