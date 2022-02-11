# A frog wants to get from point X to point Y, and can jump a fixed distance of D. Find the minimum number of frog jumps given starting point X, end point Y, and jump size D.
# This solution got 100%. There are a number of other ways to do this.
# I wasn't sure if codility would let me import the math module, so commented another solution that also seems to work. 

import math

def solution(X, Y, D):
    diff = Y-X
    minJumps = math.ceil(diff / D)
    #remainder = (diff % D) / D
    #minJumps = int(actualJumps + (1-remainder))
    return minJumps
