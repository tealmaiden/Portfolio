#Write a function:

#def solution(A)

#that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

#Given A = [1, 2, 3], the function should return 4.

#Given A = [−1, −3], the function should return 1.

#Write an efficient algorithm for the following assumptions:

#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].


#This was very similar to the Perm Missing Elem task, so my answer is very similar, only accounting for the possibility of negative numbers.
#Since the question only asks for a positive number, these could be filtered out. This answer give O(N) or O(NlogN)

def solution(A):
    freq= {}
    length = len(A)

    if length == 0:
        return 1
        
    for item in A:
        if item > 0:
            if item not in freq:
                freq[item]=1
            else:
                freq[item]+=1
    
    if len(freq) == 0:
        return 1
    
    for i in range(max(A)):        
        if i+1 not in freq:
            return i+1
        else:
            pass
    
    return max(A)+1
