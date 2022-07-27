# Find the minimum index that returns the slice of the array with the lowest average. This is in the prefix sums lesson.

# This is a really difficult problem for a few reasons. It required understanding a new mathematical concept.
# My orginal versions below returned the correct answer, but were not optimal for speed, so gives 60% O(N^2). All versions use prefix sums. 
# Since we want to find the lowest index, I made a function that finds the reversed prefix sum (Right to Left) of the given array rather that Left to Right. 
# This way when the this reversed prefix array is traversed to find averages, it is easier to identify minimum indices that give minimum averages. It is hard to explain.
# I originally thought the issue was the use of a nested loop, but removing it didn't help.
# The trick to fixing the efficiency is the mathematical understanding that not every slice needs to be compared. Just the ones with lengths of 2 or 3. 
# This is because the averages of longer slices are made up of the smaller slices of 2 or 3. My uncommented answer below got 100% score O(N) efficiency.

A = [4,2,2,5,1,5,8] #1
#A = [1,1,1,1,1,1,1] #0
#A = [6,1,2,3,4,5,0] #1 
#A = [6, -3, -5, 100, -1, -100] #4
#A = [-3, -5, -8, -4, -10] #2
#A = [1,2,3,4,5,6,7] #1

def reversedPrefixSum(A):
    lengthPlus = len(A) + 1
    revPref = lengthPlus * [0]
    for i in range(1, lengthPlus, 1):
        revPref[i] = A[len(A)-i]+revPref[i-1]
    return revPref
#print(reversedPrefixSum(A))

def solution(A):
    revPref = reversedPrefixSum(A)
    minIndex = 0
    theMin = 10000
    start = 2
    ogLength = len(A)
    rounds = 0
    loops = 0
    while(rounds < ogLength-1):     
        place = start + rounds + loops 
        numerator = revPref[place] - revPref[rounds]
        denominator = 2 + loops        
        avg = numerator / denominator        
        if avg <= theMin:
            theMin = avg
            minIndex = ogLength - start - rounds - loops     
        loops += 1
        if denominator == 3 or place == ogLength:
            rounds += 1
            loops = 0
        continue
    return minIndex

print(solution(A))

#Original version checking every slice:
#correct, 60%, O(n^2) efficiency:
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

# Removing the nested loop actually didn't improve the efficiency interestingly. This solution is equivalent to the one above:
#def solution(A):
#    revPref = reversedPrefixSum(A)
#    #print("revPref: " + str(revPref))
#    minIndex = 0
#    theMin = 10000
#    length = len(A)
#    ogLength = len(A)
#    #print("starting length: " + str(length))
#    rounds = 0
#    while(length>1):
#        for i in range(length-1):
#            #print("length: " + str(length))
#            #print("revPref[rounds]: " + str(revPref[rounds]))
#            #print("revPref[length-i]: " + str(revPref[length-i]))
#            numerator = revPref[ogLength-i]-revPref[rounds]
#            avg = numerator/(length-i)
#            #print("i: " + str(i))
#            #print("avg: " + str(avg))
#            #print()
#            if avg<=theMin:
#                theMin=avg
#                minIndex = i
#        length-=1
#        rounds+=1
#        continue
#    #print("ROUNDS: " + str(rounds))
#    #print()
#    return minIndex


