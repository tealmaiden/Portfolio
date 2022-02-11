# Write a function that rotates an array A clockwise by K spaces. This got %100. 
# The tricky part for me was dealing with input larger than N, which is dealt with by the second conditional. 
# I also learned that in Python, equality is set by reference by default for arrays. Setting B=A made B identical to A in memory, which is why .copy() was needed in this method.
# There are probably other ways to do this, but this is what I came up with.

def solution(A, K):
    N = len(A)
    B = A.copy()
    for i in range(N):
        if (K == N) or (K == 0): 
            return B
        if K > N:
            K = K % N
        B[i]=A[i-K]
    return B
