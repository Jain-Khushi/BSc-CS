s = input("Enter a sentence : ")
print("Output : ",end="")
for i in s:
    if i==" ":
        print(" ",end="")
    else:
         char=ord(i)
         print(chr(char+1),end="")
       
