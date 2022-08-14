# This is a very visual problem. Count the number of pairs of intersecting discs. A disc is represented in an array A with it's center at i of each item A[i] in the array, where A[i] equals the radius. 
# It is easy to miss in the problem statement, but the intersection of a disk is when the areas of the discs intersect and not just the borders. 
# This was a point of misunderstanding at first.
# This is in the sorting section. It has been hard to see what kind of sorting would make this faster.
# The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Here is a correct solution that scores 62% due to performance. The performance is O(N^2) but is improved 12% over an earlier version.
# This solution is quite complicated. 
# It creates disc objects out of the array, sorts them by top range, compares the overlap using a variable, and, if it needs to, compares using a dictionary.
# I usually avoid using Python for objects because it is awkward. There is more information entered into the discs than is needed, but I may experiment more with it.

class disc:
  def __init__(self, center, top, bot, radius):
    self.center = center
    self.top = top
    self.bot = bot
    self.radius = radius

def solution(A):
    
    length = len(A)
    count = 0
    if length == 0:
        return count

    discs = []

    for i in range(length):
        center = i
        radius = A[i]
        bot = i - radius
        top = i + radius

        the_disc = disc(center, top, bot, radius)

        discs.append(the_disc)
    
    discs.sort(key = lambda x:(x.top, x.radius))

    minTop = discs[0].top
    previousTops = {minTop:1}

    while count <= 10000000:
        for i in range(1, length, 1):
            the_disc = discs[i]
            top = the_disc.top

            if the_disc.bot <= minTop:
                #print("radius: " + str(discs[i].radius))
                #print("center: " + str(the_disc.center))
                count += i
                #print(i)            
            else:
                for key, value in previousTops.items():
                    if key >= the_disc.bot:
                        count += value 
                        #print("hit")
            
            if top in previousTops:
                previousTops[top] += 1
            else:
                previousTops[top] = 1

        return count
    
    return -1

A = [0, 5, 2, 1, 4, 0]
A = [1, 1, 1]
A = []
A = [1, 4, 2, 8, 0, 3]


# Below is a relatively simple correct solution that is O(N^2) and gets zero performance points:
# It goes through the each disc and compares it to the discs that come after it in the array to check if they touch:

# def between (a, sandwich, b):
#     if (a <= sandwich <= b):
#         return True
#     else:
#         return False

# def solution(A):

#     count = 0     

#     while count <= 10000000:
#         for i in range(len(A)):
#             cursorTop = i + A[i]
#             cursorBot = i - A[i]

#             for j in range(i+1, len(A), 1):
#                 compTop = j + A[j]
#                 compBot = j - A[j]

#                 if between(compBot, cursorTop, compTop):
#                     count += 1
#                 elif between(compBot, cursorBot, compTop):
#                     count += 1
#                 elif between(cursorBot, compTop, cursorTop):
#                     count += 1
#                 elif between(cursorBot, compBot, cursorTop):
#                     count += 1
#         return count    
    
#     return -1

#Progression:
#https://app.codility.com/demo/results/training84G88R-8HZ/
#https://app.codility.com/demo/results/training4VWHEH-5CM/
