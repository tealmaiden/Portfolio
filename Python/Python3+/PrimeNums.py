for n in range(2, 15):
    remainder = n%2
    if remainder != 0:
        print(str(n) + " is a prime number")
    for x in range(2,n):    
        if n%x==0:
            print(str(n) + " equals " + str(int(x)) + " X " + str(n//x)) #double slash is integer divisionso that decimal places .0 are not printed. could also cast to int. 
