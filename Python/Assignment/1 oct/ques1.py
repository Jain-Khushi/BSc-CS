
list1=[2,3,4,5,3,4]
print("List of integers :",list1)
list2=[]
count=0

for i in list1:
    if i not in list2:
        count=count+1
        list2.append(i)

print("Unique items in list :",count)
    
