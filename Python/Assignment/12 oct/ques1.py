l=input("Enter the list : ")
list1=l.split()
list2=[]
for i in list1:
    if int(i)%3!=0:
        list2.append(i)

print("Output :",list2)
