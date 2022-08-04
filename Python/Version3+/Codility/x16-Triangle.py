# Return 1 if an array contains a set of 3 values that are triangular. Return 0 if not. This is in the sorting section.
# Triangular values are at positions P, Q, and R where 
# A[P] + A[Q] > A[R]
# A[Q] + A[R] > A[P]
# A[R] + A[P] > A[Q]

# My solution is a work in progress. It gives the correct answer but is O^3 efficiency because I don't yet know how to do this without a triple for-loop.
# One thing that is apparent is that if a set of values is triangular, it doesn't matter the positions they are in the array.
# This means the values can be arranged in a different way, but I don't know how that would help.

# Here is my 75% solution:
def triangle(A, P, Q, R):
    if A[P] + A[Q] > A[R] and A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q]:
        return True
    else:
        return False

def solution(A):
    length = len(A)
    P = 0
    while P <= length-3:
        for Q in range(P+1, length, 1):
            for R in range(Q+1, length, 1):
                if triangle(A, P, Q, R):
                    return 1
        P += 1
        continue
    return 0

#A = [10, 2, 5, 1, 8, 20]
A = [10, 50, 5, 1]

print(solution(A))

#https://app.codility.com/demo/results/trainingGWNNZ9-92K/
