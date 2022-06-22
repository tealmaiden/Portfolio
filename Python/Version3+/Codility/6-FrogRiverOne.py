# Basically this problem is asking to return the index of a value X in an array A as long as all previous values from 1 to X before it are present in the array. 
# It is wrapped up in a story about a frog crossing a river that is a page long and fun, but rather unhelpful for me to understand what to do on a timed test.
# There is a place for word problems, and this mad hatter approach to testing seems okay for homework occasionally, but rather unproductive with the time I have personally to learn this right now.
# It also seems unproductive to evaluating my abilities after understanding the problem statement.
# Here is my 100% solution after a few rounds of trial and error, half to do with understanding of the question and half to do with little mistakes that the sample input helped me find. 
# O(N) efficiency:


# A = [1, 3, 1, 4, 2, 3, 5, 4]
# A = [2, 2, 2, 2, 2, 2, 2, 2]
A  = [1, 3, 1, 3, 2, 1, 3]

def solution(X, A):
    freqPositions = {}
    maxPresent = False
    for i in range(len(A)):
        if A[i] not in freqPositions:
            freqPositions[A[i]] = 1
            if A[i]==X:
                maxPresent = True 
        else:
            freqPositions[A[i]] += 1
            if A[i]==X:
                maxPresent = True 
        lengthfreq = len(freqPositions)
        if lengthfreq == X and maxPresent == True:
            return i
    return -1   
