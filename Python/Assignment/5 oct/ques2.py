s=input("Enter the string :")
l=len(s)
v_count=0
c_count=0
u_count=0
l_count=0
for i in s:
    if i.isupper():
        u_count=u_count+1
    elif i.islower():
            l_count=l_count+1

    i=i.upper()
    vowels='AEIOU'

    if i in vowels:
        v_count=v_count+1
    
    elif ord(i) >= 65 and ord(i) <= 90:
            c_count+=1
        

print("Number of vowels :",v_count)
print("Number of consonants :",c_count)
print("Number of uppercase letters :",u_count)
print("Number of lowercase letters :",l_count)
