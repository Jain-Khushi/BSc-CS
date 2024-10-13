#(a)

import math
 
# Function to get the series
def Series( x , n ):
    sum = 1
    term = 1
    y = 2
     
    # Sum of n-1 terms starting from 2nd term
    for i in range(1,n):
        fact = 1
        for j in range(1,y+1):
            fact = fact * j
         
        term = term * (-1)
        m = term * math.pow(x, y) / fact
        sum = sum + m
        y += 2
     
    return sum
 
# Driver Code
print("(a)")
x = int(input("Enter the Value for x: "))
n = int(input("Enter the Value for n: "))
print("Sum of series is :",Series(x, n))


#(b)

import math
 
# Function to get the series
def Series( x , n ):
    sum = 1
    term = 1
    y = 2
     
    # Sum of n-1 terms starting from 2nd term
    for i in range(1,n):
        fct = 1
        for j in range(1,y+1):
            fct = fct * j
         
        term = term * (1)
        m = term * math.pow(x, y) / fct
        sum = sum + m
        y += 2
     
    return sum
 
# Driver Code
print("\n\n(b)")
x = int(input("Enter the Value for x: "))
n = int(input("Enter the Value for y: "))
print("Sum of series is :",Series(x, n))
