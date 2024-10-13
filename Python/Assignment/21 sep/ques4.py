# Function to find the sum of the series: [1+(1+2)+(1+2+3)+–+(1+2+3+–+n)].

n = int(input("Enter value of n: "))

sum = n*(n+1)*(2*n+4)/12
print("Sum of the series is :",sum)
