# DNA is a string of nucleotides that can be literally represented by a string S.
# Nucleotides (A, C, G, T) have the following impact factors (1, 2, 3, 4).
# Write an efficient function that finds the minimum impact factor within a given range on a strand of DNA.
# The beginning position in the range is given by an integer in the array P containing M values.
# The ending position in the range is given by an integer in the array Q, also containing M values.
# The function takes S, P, and Q and returns an array of minimum impact factors for each range.
# This is in the prefix sums lesson.

# S = "CAGCCTA"
# P = [2,5,0]
# Q = [4,5,6]
S = "TC"
P = [0,0,1]
Q = [0,1,1]

# 100% solution O(N+M). This is another solution in the prefix sums section that doesn't use prefix sums, but still works well.
# I might return to this later to see if there is a way to use prefix sums or if it just a distraction.
# The optimization over earlier versions was to check for the presence of each impact in the desired sequence one at a time, starting with the smallest one (A),
# and just set the min value to the smallest present value.
# Earlier versions below this solution compare all of the values in the sequence to find the min.

def solution(S, P, Q):
    length = len(P)    
    nucleoImpactDictionary = {'A':1, 'C':2, 'G':3, 'T':4}
    impactList = []

    for i in range(length):
        p=P[i]
        q=Q[i]  
        
        sequence=S[p:q+1]
        if "A" in sequence:
            minFactor=nucleoImpactDictionary['A']
        elif "C" in sequence:
            minFactor=nucleoImpactDictionary['C']
        elif "G" in sequence:
            minFactor=nucleoImpactDictionary['G']
        elif "T" in sequence:
            minFactor=nucleoImpactDictionary['T']

        impactList.append(minFactor)
    return impactList


# # This is an earlier version. Accurate, but slow solution:
# def dummySolution(S, P, Q):
#      length = len(P)    
#      nucleoImpactDictionary = {'A':1, 'C':2, 'G':3, 'T':4}
#      impactList = []
#      for i in range(length):
#          p=P[i]
#          q=Q[i]         
#          minFactor = 4

#          for i in range(p, q+1, 1): 
#             nucleoImpact = nucleoImpactDictionary[S[i]]
#             if nucleoImpact < minFactor:
#                 minFactor = nucleoImpact
                 
#          impactList.append(minFactor)
#      return impactList

# print("dummy solution: " + str(dummySolution(S, P, Q)))

# # An equivalent slow solution as the one above, but more concise. It seems the min() function is equivalent to using a for loop:
# def dummySolution2(S, P, Q):
#     length = len(P)    
#     nucleoImpactDictionary = {'A':1, 'C':2, 'G':3, 'T':4}
#     impactList = []
#     STranslated = []    

#     for c in S:
#         STranslated.append(nucleoImpactDictionary[c])

#     for i in range(length):
#         p=P[i]
#         q=Q[i]  
        
#         minFactor = min(STranslated[p:q+1])
     
#         impactList.append(minFactor)
#     return impactList

# print("dummySolution2: " + str(dummySolution2(S, P, Q)))
