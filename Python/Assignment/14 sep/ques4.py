num=int(input("Enter a number : "))
alpha=65 #ASCII value of alphabet A

for i in range(num,0,-1):
    for j in range(0,i):
        char=chr(alpha)
        print(char,end=' ')
        
    alpha+=1
    print("")
