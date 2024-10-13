L1=input("Enter the list : ")
list1=L1.split()
list2=[[ ]]
for i in range(len(list1)+1):
    for j in range(i+1,len(list1)+1):
        sub=list1[i:j]
        list2.append(sub)

print("Sublist :",list2)
