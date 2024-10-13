def linear_search(list1, x):
  
    for i in range(len(list1)):
  
        if list1[i] == x:
            return i
  
    return -1


def binary_search(list1, x):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
 
        mid = (high + low) // 2
 
        if list1[mid] < x:
            low = mid + 1
 
        elif list1[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1

def final_search(result):
           if result != -1:
               print("\nName is present at index", str(result))
           else:
               print("\nName is not present in array")
               

def bubbleSort(list1):
    n = len(list1)
    for i in range(n):
        swapped = False
 
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1] :
                list1[j], list1[j+1] = list1[j+1], list1[j]
                swapped = True

        if swapped == False:
            break
        


def selectionSort(list1):
    for i in range(len(list1)):
        min_idx = i
        for j in range(i+1, len(list1)):
            if list1[min_idx] > list1[j]:
               min_idx = j
                     
        list1[i], list1[min_idx] = list1[min_idx], list1[i]


def insertionSort(list1):
    for i in range(1, len(list1)):
  
        key = list1[i]
        j = i-1
        while j >=0 and key < list1[j] :
                list1[j+1] = list1[j]
                j -= 1
        list1[j+1] = key
        
    

def final_sort(result):
    print ("\nSorted array : ",end='')
    for i in range(len(list1)):
        print(list1[i],end=' ')
    

def search():
    while True:
        print("\nSelect the search you want to use :\n1. Linear Search\n2. Binary Search\n")
        choice=int(input("Enter your choice : "))
        if choice==1:
           result= linear_search(list1,x)
           final_search(result)
           sort()
           break
        elif choice==2:
           print("To implement binary search ,we need to sort the list first.\n")
           sort()
           result= binary_search(list1,x)
           final_search(result)
           break
        else:
           print("Invalid choice!!")


def sort():
    while True:
        print("\nSelect the sort you want to use :\n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n")
        choice=int(input("Enter your choice : "))
    
        if choice==1:
           result=bubbleSort(list1)
           final_sort(result)
           break
        elif choice == 2:
           result=selectionSort(list1)
           final_sort(result)
           break
        elif choice == 3:
           result=insertionSort(list1)
           final_sort(result)
           break
        else:
            print("Invalid choice!!")
    
    
l=input("Enter the names of students(separated by space) :")
list1=l.split()

print("List of names :",list1)
x=input("Enter the name to be searched :")
search()

   

  
 





        
    
