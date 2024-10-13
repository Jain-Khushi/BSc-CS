# iterative code for insertion sort

def insertionSort(arr):
    for i in range(1, len(arr)):
  
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
  

# recursive code for insertion sort

def insertionSortRecursive(arr,n):
    if n<=1:
        return
    
    insertionSortRecursive(arr,n-1)
    last = arr[n-1]
    j = n-2
    
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
 
    arr[j+1]=last

   
# Driver code to test above
arr = [12, 11, 13, 5, 6]
n=len(arr)

print("Original array :",arr)

print("\n      Insertion Sort")

insertionSort(arr)
print ("\nSorted array using iterative code :")
for i in range(len(arr)):
    print(arr[i],end=' ')

insertionSortRecursive(arr,n)
print ("\n\nSorted array using recursive code :")
for i in range(len(arr)):
    print(arr[i],end=' ')
