# This is a very visual problem. Count the number of pairs of intersecting discs. A disc is represented in an array A with it's center at i of each item A[i] in the array, where A[i] equals the radius. 
# It is easy to miss in the problem statement, but the intersection of a disk is when the areas of the discs intersect and not just the borders. 
# This was a point of misunderstanding at first.
# This is in the sorting section. It has been hard to see what kind of sorting would make this faster.
# The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Here is a correct solution that scores 68% due to performance. The performance is O(N^2) but is improved 18% over the first version.
# This solution creates disc objects out of the array to keep track of their top and bottom, and then sorts them by bottom. 
# It then iterates through the discs while keeping track of the tops as it goes and sorts this list of tops.
# It compares the bottom of each disc to the list of tops. 
# If the bottom of the disc is less than the minimum top, it that means it intersects with all discs below it, and the count can be increased by the position of the disc.
# If not, the count can be set to the disc position minus the number of previous tops that are less than the disc bottom.
# I usually avoid using Python for objects because it is awkward. There is more information entered into the discs than is needed, but I may experiment more with it.

class disc:
  def __init__(self, top, bot, radius):
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
        radius = A[i]
        bot = i - radius
        top = i + radius               

        the_disc = disc(top, bot, radius)
        discs.append(the_disc)
    
    discs.sort(key = lambda x:(x.bot, x.radius)) #sort by bottom, then radius. may not really need to sort by radius, but it is good to know it is possible to do.

    while count <= 10000000:

        topsTracker = [discs[0].top]        

        for i in range(1, length, 1):
            
            the_disc = discs[i]
            
            #This first if statement isn't really needed. It just makes it easier to explain the next part:
            if the_disc.bot <= topsTracker[0]:
                count += i       
                topsTracker.append(the_disc.top)
                topsTracker.sort()

            else:
                subtract = 0
                for j in range(len(topsTracker)):
                    if topsTracker[j] < the_disc.bot:
                        subtract += 1
                    else:
                        count += (i-subtract)
                        topsTracker.append(the_disc.top)
                        topsTracker.sort()
                        break         
            
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
#https://app.codility.com/demo/results/trainingYB42VU-7U2/
