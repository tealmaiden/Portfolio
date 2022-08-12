# This is a very visual problem. Count the number of pairs of intersecting discs. A disc is represented in an array A with it's center at i of each item A[i] in the array, where A[i] equals the radius. 
# It is not stated in the problem, but the intersection of a disk is when the areas of the discs intersect and not just the borders. This was a point of misunderstanding at first.
# This is in the sorting section, but I don't yet see what kind of sorting would make this faster. Sorting by size would change the positions.


# Below is a correct solution that is O(N^2). It is a work in progress.
# It then goes through the each disc and compares it to the discs that come after it in the array to check if they touch:

def between (a, sandwich, b):
    if (a <= sandwich <= b):
        return True
    else:
        return False

def solution(A):

    count = 0     

    if count <= 10000000:
        for i in range(len(A)):
            cursorTop = i + A[i]
            cursorBot = i - A[i]

            for j in range(i+1, len(A), 1):
                compTop = j + A[j]
                compBot = j - A[j]

                if between(compBot, cursorTop, compTop):
                    count += 1
                elif between(compBot, cursorBot, compTop):
                    count += 1
                elif between(cursorBot, compTop, cursorTop):
                    count += 1
                elif between(cursorBot, compBot, cursorTop):
                    count += 1
    else:
        return -1

    return count
  
#https://app.codility.com/demo/results/trainingD6THUW-N38/
#https://app.codility.com/demo/results/trainingGFRXDX-QHJ/
