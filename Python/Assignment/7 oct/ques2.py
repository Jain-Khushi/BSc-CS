l=input("Enter the elements of list(separated by space) : ")
list1=l.split()
print("Input list :",list1)
list2 = []

[list2.append(i) for i in list1 if i not in list2]
print("New list :",list2)
