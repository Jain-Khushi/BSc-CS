def vowels(s1):
    char='*'
    v='aeiouAEIOU'
    for i in v:
        s1=s1.replace(i,char)
        
    return s1

s=input("Enter the string : ")
print("New string :",vowels(s))
