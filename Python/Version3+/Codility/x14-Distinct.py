# This in the sorting lesson. Return the number of distinct elements in a list. I found it simplest to solve this with a frequency table.
# This got 100%, O(NlogN) or O(N):

def solution(A):
    freq = {}
    for item in A:
        if item in freq:
            freq[item]+=1
        else:
            freq[item] = 1
    length = len(freq)
    return length


#https://app.codility.com/demo/results/trainingWRCC5E-VGK/
