# In a permutation of consecutive integers starting with 1, print the missing element. Assume there is one missing element. E.g. in in [3,5,1,2] the missing element is 4.
# This solution got 100%. It took a few tries to realize that it wanted me to return a number above the maximum number in the case that a sequence did not have a missing element.
# I don't think this question was stated very well because such a case of a non-missing element seems to be explicitly excluded in the question statement. 
# This was another efficiency test, which I again handled with a dictionary.

def solution(A):
    freq= {}
    length = len(A)
    if length == 0:
        return 1
        
    for item in A:
        freq[item] = 1

    for i in range(max(A)):
        if i+1 not in freq:
            return i+1
        else:
            pass
    
    return max(A)+1
