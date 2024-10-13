def count_vowels(s,v_count):
    for i in range(0,l):
         if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U" or s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
             v_count=v_count+1
    print("Number of vowels is :",v_count)
        
s=input("Enter a string : ")
l=len(s)
v_count=0
count_vowels(s,v_count)

