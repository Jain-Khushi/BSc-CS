s=input("Enter the string :")
l=len(s)
v_count=0
c_count=0
u_count=0
l_count=0
for i in range(0,l):
    if s[i].isupper():
        u_count=u_count+1
    elif s[i].islower():
            l_count=l_count+1

    if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U" or s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        v_count=v_count+1
    else:
        c_count=c_count+1

print("Number of vowels :",v_count)
print("Number of consonants :",c_count)
print("Number of uppercase letters :",u_count)
print("Number of lowercase letters :",l_count)

