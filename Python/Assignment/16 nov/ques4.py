def insertionSort(list1):
    for i in range(1, len(list1)):
  
        key = list1[i]
        j = i-1
        while j >=0 and key < list1[j] :
                list1[j+1] = list1[j]
                j -= 1
        list1[j+1] = key
        
    
def final_sort(result):
    print ("\nSorted array using insertion sort : ",end='')
    for i in range(len(list1)):
        print(list1[i],end=' ')
    
    
l=input("Enter the list of strings(separated by space) :")
list1=l.split()

print("List of names :",list1)
result=insertionSort(list1)
final_sort(result)
   

  
 





        
    
