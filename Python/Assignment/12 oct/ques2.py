l=input("Enter the list : ")
list1=l.split()
count=0
ele=int(input("Enter the element : "))
for i in list1:
    if int(i)==ele:
        count+=1

print("Count :",count)
