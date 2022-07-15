# DNA is a string of nucleotides that can be literally represented by a string S.
# Nucleotides (A, C, G, T) have the following impact factors (1, 2, 3, 4).
# Write an efficient function that finds the minimum impact factor within a given range on a strand of DNA.
# The beginning position in the range is given by an integer in the array P containing M values.
# The ending position in the range is given by an integer in the array Q, also containing M values.
# The function takes S, P, and Q and returns an array of minimum impact factors for each range.

S = "AAAAAAAAA"
S = "CAGCCTA"
P = [2,5,0]
Q = [4,5,6]

# This is a work in progress. Accurate, but slow solution:
def dummySolution(S, P, Q):
     length = len(P)    
     nucleoImpactDictionary = {'A':1, 'C':2, 'G':3, 'T':4}
     impactList = []
     for i in range(length):
         p=P[i]
         q=Q[i]         
         minFactor = 4

         if p==q:
             nucleoImpact = nucleoImpactDictionary[S[p]]
             if nucleoImpact < minFactor:
                 minFactor = nucleoImpact
         else:
             for i in range(p, q, 1): 
                 nucleoImpact = nucleoImpactDictionary[S[i]]
                 if nucleoImpact < minFactor:
                     minFactor = nucleoImpact
                 
         impactList.append(minFactor)
     return impactList


print("dummy solution: " + str(dummySolution(S, P, Q)))
