# Find the minimum index that returns the slice of the array with the lowest average. This is in the prefix sums lesson.

# This is a really difficult problem. The following code is a work in progress.
# It returns the correct answer, but is not optimal for speed, so gives 60%. It uses prefix sums. I thought the issue was the use of a nested loop, but removing it didn't help (see commented solution below).
# Since we want to find the lowest index, I made a function that finds the reversed prefix sum (Right to Left) of the given array rather that Left to Right. 
# This way when the this reversed prefix array is traversed to find averages, it is easier to inentify minimum indices that give minimum averages. It is hard to explain.
# Not yet sure how to get rid of the nested loop for checking every possible slice.

A = [4,2,2,5,1,5,8] #1
#A = [1,1,1,1,1,1,1] #0
#A = [6,1,2,3,4,5,0] #1 
#A = [6, -3, -5, 100, -1, -100]
#A = [-3, -5, -8, -4, -10] #2
#A = [1,2,3,4,5,6,7]

def reversedPrefixSum(A):
    lengthPlus = len(A) + 1
    revPref = lengthPlus * [0]
    for i in range(1, lengthPlus, 1):
        revPref[i] = A[len(A)-i]+revPref[i-1]
    return revPref

#print(reversedPrefixSum(A))

def minFromBack(revPref, length):
    for i in range(0, length-2, 1):
        revPref[length] - revPref[i]

def solution(A):
    revPref = reversedPrefixSum(A)
    #print("revPref: " + str(revPref))
    minIndex = 0
    theMin = 10000
    length = len(A)
    ogLength = len(A)
    #print("starting length: " + str(length))
    rounds = 0
    while(length>1):
        for i in range(length-1):
            #print("length: " + str(length))
            #print("revPref[rounds]: " + str(revPref[rounds]))
            #print("revPref[length-i]: " + str(revPref[length-i]))
            numerator = revPref[ogLength-i]-revPref[rounds]
            avg = numerator/(length-i)
            #print("i: " + str(i))
            #print("avg: " + str(avg))
            #print()
            if avg<=theMin:
                theMin=avg
                minIndex = i
        length-=1
        rounds+=1
        continue
    #print("ROUNDS: " + str(rounds))
    #print()
    return minIndex

print(solution(A))

# Removing the nested loop actually didn't improve the efficiency interestingly. This solution is equivalent to the one above:
#def solution(A):
#    revPref = reversedPrefixSum(A)
#    minIndex = 0
#    theMin = 10000
#    length = len(A)
#    ogLength = len(A)
#    rounds = 0
#    loops = 0
#    while(length>1):        
#        numerator = revPref[ogLength-loops]-revPref[rounds]
#        denominator = length-loops        
#        avg = numerator/denominator        
#        if avg<=theMin:
#            theMin = avg
#            minIndex = loops     
#        loops+=1
#        if denominator==2:
#            length-=1
#            rounds+=1
#            loops = 0
#        continue
#    return minIndex


