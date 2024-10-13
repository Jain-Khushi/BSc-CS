#iterative code for linear search
def linear_search(list1, x):
  
    for i in range(len(list1)):
  
        if int(list1[i]) == x:
            return i
  
    return -1


#iterative code for binary search
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


#recursive code for linear search
def linear_search_rec(list1, l, r, x):
    if r < l:
        return -1
    if int(list1[l]) == x:
        return l
    if int(list1[r]) == x:
        return r
    return linear_search_rec(list1, l+1, r-1, x)


#recursive code for binary search
def binary_search_rec(list1, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2

        if int(list1[mid]) == x:
            return mid
        elif int(list1[mid]) > x:
            return binary_search_rec(list1, low, mid - 1, x)
        else:
            return binary_search_rec(list1, mid + 1, high, x)
 
    else:
        return -1
    


def final(result):
           if result != -1:
               print("Element is present at index", str(result))
           else:
               print("Element is not present in array")

        
#Driver code
l=input("Enter the array of elements(separated by space) : ")
list1=l.split()
x=int(input("Enter the element to be searched : "))

print("\nIterative method :\n")

print("Using Linear Search :")
result= linear_search(list1,x)
final(result)

print("\nUsing Binary Search :")
result= binary_search(list1,x)
final(result)

print("\nRecursive method :\n")

print("Using Linear Search :")
result= linear_search_rec(list1,0,len(list1)-1,x)
final(result)

print("\nUsing Binary Search :")
result= binary_search_rec(list1,0,len(list1)-1,x)
final(result)
       

