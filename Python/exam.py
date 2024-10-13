def check_Eligibility(n):
    '''Functon checking eligibility of a number'''
    if (n==1):
        print("Sorry")
        return False
    elif (n==2):
        print("Proceed for Printing")
        return True;
    elif (n>29):
        print("Sorry")
        return False
    else:
        for x in range(2,n):
            if(n % x==0):
                print("Sorry")
                return False
        print("Proceed for Printing")
        return True  



def displayPattern(n):
    '''Function checking eligibility of a number and on that basis printing the pattern'''
    if(check_Eligibility(n)):
        idx=ord('A')
        for i in range (0,n):
            cs=chr(idx+i)
            for j in range (0,n-i-1):
                print(" ",end="")
            print(cs,end="")
            for j in range (0,2*i-1):
                print("*",end="")
            if(i!=0):
                print(cs)
            else:
                print()
    else:
        print("Pattern Not Possible")

a = int(input("Enter a Number: "))           
print(check_Eligibility(a))

n=int(input("Enter a number : "))
displayPattern(n)
