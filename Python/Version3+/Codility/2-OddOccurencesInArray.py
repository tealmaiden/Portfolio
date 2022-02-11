# Given an array of ints A containing duplicates, return the int that does not have any pair. Assume there is only one in the set that doesn't have a pair.
# This solution got 100%. In addition to accuracy it had a good performance, probably because of the use of a dictionary.

def solution(A):

    numcounts = {}

    for num in A:
        if num not in numcounts:
            numcounts[num]=1
        else:
            numcounts[num]+=1
    
    for num in numcounts:
        if numcounts[num] % 2 > 0:
            return num
