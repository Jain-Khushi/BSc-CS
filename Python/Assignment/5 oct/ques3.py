s=input("Enter a string : ")
char=input("Enter the character : ")
count=0

for i in s:
    if i==char:
        count+=1

print("Count of the character in the string :",count)
