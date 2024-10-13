def sum67(list1):
    print(list1)
    sum=0

    for i in range(len(list1)):
       if int(list1[i])==6:
          while int(list1[i])!=7:
            list1.pop(i)
          list1.pop(i)
          break
                   
    for i in list1:
      sum=sum+int(i)
    
    print("The sum is :",sum)
    print()
    
sum67([1,2,2])
sum67([1,2,2,6,99,99,7])
sum67([1,1,6,7,2])
