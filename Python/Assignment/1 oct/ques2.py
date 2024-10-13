list1=[2,3,4,5,3,4]
print("List of integers :",list1)
list2 = []

[list2.append(i) for i in list1 if i not in list2]
print("Sum of unique elements of the list :", sum(list2))
