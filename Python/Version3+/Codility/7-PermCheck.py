# Check if an array is a permutation, assuming the input is a positive number from 1 to N.
# This got 100%, O(N) or O(NlogN), 19 min:

# contains a sequence of numbers from 1 to N
# each number in the sequence appears only once
# can be in any order


def solution(A):
    freq ={}
    for item in A:
        if item not in freq:
            freq[item]=1
        else:
            freq[item]+=1
    maximum = max(freq)
    if len(freq) == maximum and sum(freq.values()) == maximum:
        return 1
    else:
        return 0
