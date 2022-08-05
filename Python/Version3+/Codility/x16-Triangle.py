# Return 1 if an array contains a set of 3 values that are triangular. Return 0 if not. This is in the sorting section.
# Triangular values are at positions P, Q, and R where 
# A[P] + A[Q] > A[R]
# A[Q] + A[R] > A[P]
# A[R] + A[P] > A[Q]

# My solution is a work in progress. It gives the correct answer but is O^3 efficiency because I don't yet know how to do this without a triple loop.
# One thing that is apparent is that if a set of values is triangular, it doesn't matter the positions they are in the array.
# This means the values can be arranged in a different way, but I don't know if that is the key to this problem.
# After some experimenting, I found that rearranging the list in a certain out-of-order way sped it up in some cases because it allowed for fewer comparisons before returning an answer.
# This sped up my original answer a little bit and raised my score about 6%.

# Here is my 81% solution:
def trianglesort(A):
    A.sort(reverse=True)
    length = len(A)
    B = [0] * length
    for i in range(length):
        if i%2 == 0:
            B[int(length-1-i/2)] = A[i]
        elif (i+1)%2 == 0:
            B[int((i+1)/2-1)] = A[i]
    return B

def solution(A):
    length = len(A)
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

#Progression:
#https://app.codility.com/demo/results/trainingGWNNZ9-92K/
#https://app.codility.com/demo/results/trainingV3J7PX-YZJ/
