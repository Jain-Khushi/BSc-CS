# iterative code for selection sort

def selectionSort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
               min_idx = j
                     
        A[i], A[min_idx] = A[min_idx], A[i]


# recursive code for selection sort

def minIndex( A , i , j ):
    if i == j:
        return i
    k = minIndex(A, i + 1, j)
    return (i if A[i] < A[k] else k)

def recurSelectionSort(A, n, index = 0):
    if index == n:
        return -1
    k = minIndex(A, index, n-1)
    if k != index:
        A[k], A[index] = A[index], A[k]
    recurSelectionSort(A, n, index + 1)

# Driver code
A = [64, 25, 12, 22, 11]
n = len(A)
 
print("Original array :",A)
print("\n       Selection Sort")
selectionSort(A)
print ("\nSorted array using iterative code : ")
for i in range(len(A)):
    print(A[i],end=' ')
    
recurSelectionSort(A, n)
print ("\n\nSorted array using recursive code : ")
for i in A:
    print(i, end = ' ')
     
