def sum(n):
    if n==0:
        return 0
    else:
        return (n%10 + sum(int(n/10)))
    
n=int(input("Enter the number : "))
val=sum(n)
print("Sum of the digits is : ",val)
