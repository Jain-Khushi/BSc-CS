#Question 2
target =input("Enter target string: ")
insert =input("Enter string to be inserted: ")
list =target.split()
list.insert(1, insert)
for i in list:
  print(i, end=" ")
