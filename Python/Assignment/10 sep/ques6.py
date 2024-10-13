string1=input("Enter string 1 :")
string2=input("Enter string 2 :")
count,j=0,0

# loop executes till length of str1 and 
# stores value of str1 character by character 
# and stores in i at each iteration.

for i in string1:
    
        #this will check if character extracted from
        # str1 is present in str2 or not(str2.find(i)
        # return -1 if not found otherwise return the 
        # starting occurrence index of that character
        # in str2)
        
        if string2.find(i)>=0 :
            count+=1
        j+=1

print("Number of matching characters in both the strings is :",count)
