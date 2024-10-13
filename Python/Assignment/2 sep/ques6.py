print("(i)\n")

rows=5
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=' ')
    print()
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("*",end=' ')
    print()

print()


print("(ii)\n")

alpha = 65 #ASCII value of alphabet A
for i in range(0,5):
    for j in range(0,i+1):
        char=chr(alpha)
        print(char,end=' ')
        alpha+=1
    print(" ")


