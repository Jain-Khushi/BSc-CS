def hcf(first,second):
    i=1
    if first>second:
        small=second
    else:
        small=first

    while i<=small:
        if first%i==0 and second%i==0:
            gcd=i
        i=i+1

    return gcd

def lcm(first,second):
    return (first / hcf(first,second))* second
    

first=int(input("Enter the first number :"))
second=int(input("Enter the second number :"))
print("The least common multiple(LCM) is :",lcm(first,second))
print("The highest common factor (HCF) is :",hcf(first,second))
