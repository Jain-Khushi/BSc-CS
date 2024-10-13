n=int(input("Enter number of elements in list : "))
list1=[]
print("Enter items of list : ")
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print("List :",list1)

list2=[]
length=len(list1)
list2=[sum(list1[0:x]) for x in range(0,length+1)]
print("Output :",list2[1:])


 
