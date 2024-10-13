l1=input("Enter the original list : ")
list1=l1.split()
ele=input("Enter the character : ")
list2=[]
for i in list1:
    for j in i:
        if j==ele:
            list2.append(i)

print("Items start with",ele,"from the said list :",list2)
