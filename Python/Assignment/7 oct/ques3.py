L1=input("Enter list 1 : ")
list1=L1.split()
L2=input("Enter list 2 : ")
list2=L2.split()

list3 = [int(i) for i in list1 + list2 if i not in list1 or i not in list2]
            
list3.sort()
print("Output :",list3)
