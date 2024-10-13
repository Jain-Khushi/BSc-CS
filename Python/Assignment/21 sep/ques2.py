num=int(input("Enter the number : "))
print("Even factors of",num,"are :")
for i in range(1,num+1):
    if(num%i == 0):
        if(i%2 == 0):
            print(i,end=" ")
