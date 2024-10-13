n=int(input("Enter a number : "))
list1=[]

for i in range(0,n):
    list1.append([])
    for j in range(1,6):
        list1[i].append((i+1)*j)

print("Output :",list1)


