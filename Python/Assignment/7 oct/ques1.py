l=input("Enter the list : ")
list1=l.split()

print("Input list :",list1)

length=len(list1)
count=0
list2=[]

print("\n------ Operations on list ------")
#(a)
print("\na)Checking if all elements in list are numbers or not:")
a = all(i.isdigit() for i in list1)
if a:
    print("All elements are numbers.")
else:
    print("All elements are not numbers.")
    
    
#(b)
print("\nb)If it is a numeric list,then counting number of odd values in it:")
if a:
    for i in list1:
        if int(i)%2 !=0 :
            count+=1
    print("Count of odd numbers :",count)
else:
    print("It is not a numeric list.")
    

#(c)
print("\nc)If list contains all Strings,then display largest String in the list:")
b = all(i.isalpha() for i in list1)
if b:
    print("Largest string :",max(list1))
else:
    print("All elements are not strings.")
    
    
#(d)
print("\nd)Displaying list in reverse form:")
print(list1[::-1])


#(e)
index=0
print("\ne)Find a specified element in list:")
ele=input("Enter the element to be searched : ")
for i in list1:
    if i==ele:
        index=1
if index==1:
    print("Element is present in the list.")
else:
    print("Element is not present in the list.")
    
        
#(f)
p=0
print("\nf)Remove the specified element from the list:")
ele1=input("Enter the element to be removed : ")
list2=list1.copy()
for i in list2:
    if i==ele1:
        p=1
        list2.remove(ele1)
        print("New list :",list2)
if p==0:
     print("Element is not present in the list.")
    
       
#(g)
print("\ng)Sort the list in descending order:")
list1.sort(reverse=True)
print(list1)


#(h)
print("\nh)Accept 2 lists and find the common members in them:")
lA = input("Enter first list : ")
listA = lA.split()
lB = input("Enter the second list : ")
listB = lB.split()
print("Common members :",end='')
           
for i in listA:
    for j in listB:
           if i==j:
              print(i,end=' ')






