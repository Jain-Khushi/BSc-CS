def deleteChar(s,char):
    s1=s.replace(char,"")

    return s1

s=input("Enter a string : ")
char=input("Enter the character : ")
print("New string :",deleteChar(s,char))
