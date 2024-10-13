string=input("Enter a string : ")
s=string.title().split(" ",1)

res=" "
for i in s:
    res += i[ :-1] + i[-1].upper() + " "
    
print("Output :",res)
