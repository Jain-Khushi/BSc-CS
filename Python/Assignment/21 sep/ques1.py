n=int(input("Enter a number : "))
count=0

#converting to binary
bin="{0:b}".format(n)
print("Binary expansion of" , n , "is :", bin)
num=int(bin)


#counting 1's
while num!=0:
    rem = num%10
    if rem == 1:
        count=count+1
    num = num//10

#checking if number is evil or not
if count%2 == 0:
    print("The number is an Evil Number.")
else:
    print("The number is an Odious Number(not an evil number).")
    
