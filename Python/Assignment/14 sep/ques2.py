n=int(input("Enter the value of n : "))
a,b=0,1
print("Fibonacci Series is : ",a,b,end=' ')
i=3
while(i<=n):
    next=(a+b)
    print(next,end=' ')
    a=b
    b=next
    i+=1
    
