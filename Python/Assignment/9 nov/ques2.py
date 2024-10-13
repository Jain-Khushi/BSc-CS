def linear_search(list1, x):
  
    for i in range(len(list1)):
  
        if int(list1[i]) == x:
            return i
  
    return -1


def binary_search(list1, x):
    low = 0
    high = len(list1) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if int(list1[mid]) < x:
            low = mid + 1
 
        elif int(list1[mid]) > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1
 

def final(result):
           if result != -1:
               print("Element is present at index", str(result))
           else:
               print("Element is not present in array")
        

l=input("Enter the array of elements(separated by space) : ")
list1=l.split()
x=int(input("Enter the element to be searched : "))

while True:
    print("\n     MENU     \n1. Linear Search\n2. Binary Search\n")
    choice=int(input("Enter your choice : "))

    if choice==1:
        result= linear_search(list1,x)
        final(result)
        break
    elif choice==2:
        result= binary_search(list1,x)
        final(result)
        break
    else:
        print("Invalid choice!!")
    

