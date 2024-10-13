#iterative code for bubble sort
def bubbleSort(arr,n):
    for i in range(n):
        swapped = False
 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break


# Recursive Bubble sort 
def bubbleSort_rec(arr,n):
    if(n>0):
        for i in range(0,n):
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        bubbleSort_rec(arr, n - 1)
        
        
#Driver code          
arr = [64, 34, 25, 12, 22, 11, 90]
n=len(arr)
print("Original array : \n",arr)
bubbleSort(arr,n)

print("\n      Bubble Sort")

print ("\nSorted array using iterative code :")
for i in range(len(arr)):
    print(arr[i],end=" ")

bubbleSort_rec(arr,n-1)
print("\n\nSorted array using recursive code :"); 
for i in range(0, len(arr)): 
    print(arr[i], end=' ') 
