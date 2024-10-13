input_dict = {'first':{'a':7,'b':9,'c':12}, 'second':{'a':15,'b':19,'c':20}
              ,'third': {'a':5,'b':10,'c':2}}

a = input("Enter the key: ")
list1 = []
for key in input_dict:
    if a in input_dict[key]:
        list1.append(input_dict[key][a])
print("Output: ",list1)
