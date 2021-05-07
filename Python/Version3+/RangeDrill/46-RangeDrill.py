
##range(start, stop, step)

##1. Start  IDLE  and  use  the Python  range()  function  with  one  parameter  to 
##display  the following:
##0
##1
##2
##3

print('Drill 1:')
for i in range(4):
    print(i) 
##note: range(0,4) achieves the same result.
    
##2. Use the Python range() function with 3 parameters to display the following:
##3
##2
##1
##0

print('')
print('Drill 2:')
for i in range(3,-1,-1):
    print(i) 
##note: If 0 is used instead for the stop, the range ends at 1.


##3. Use the Python range() function with 3 parameters to display the following:
##8
##6
##4
##2

print('')
print('Drill 3:')
for i in range(8,1,-2):
    print(i) 
##note: range(8,0, -2) achieves the same result.

##4. Extra - Converting tuple to range
print('')
print('Extra:')
tuple1=(3,2,1,0)
for i in range(4):
    print(tuple1[i])
