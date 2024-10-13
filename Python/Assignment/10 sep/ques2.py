def fib(val):
    if val==0:
        return 0
    elif val==1:
        return 1
    else:
        return fib(val-2)+fib(val-1)
    
val=int(input("Enter the value of n : "))
term=fib(val)
print("Fibonacci term is :",term)
