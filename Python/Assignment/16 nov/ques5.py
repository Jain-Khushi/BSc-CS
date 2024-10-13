n=int(input("Enter the number of elements : "))
l=input("Enter the elements of list(separated by space) : ")
list1=l.split()
print("Entered list is :",list1)
s=0
print("Cumulative sum list : [",end='')
for i in range(0,n):
    s = s+int(list1[i])
    print(s,end=' ')
print("]")
    
