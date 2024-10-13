# QUESTION 2

str1="Ronald Brown"
str2="Richard Brown"
str3="Harry/* Potter% is ^a fictional !! character-&"

# part 1
def append_Strings():
    str4 = str1 + str2
    print("Appended String: ",str4,"\n")
    return str4

str4 = append_Strings()

# part 2
lowIdx , highIdx = 0, len(str4)
strTemp = ""
for i in str4:
    if(i>='a' and i<='z'): strTemp += i

for i in str4:
    if(i>='A' and i<='Z'): strTemp += i

str4 = strTemp

print("Arranged String : ",str4,"\n")

for i in range(0,len(str4)):
    if(str4[i]=='r'):
        if(i+1<len(str4) and str4[i+1]=='o'):
            if(i+2<len(str4) and str4[i+2]=='w'):
                print("row has occured between" , i+1 , " and ", i+3)

print("\n")

# part 3
str3 = ''.join(char for char in str3 if char.isalnum())
print("str3 after removing special symbols : ",str3,"\n\n\n")


List1 = [5,10,15,20,25,30,35]
List2 = [10,20,30,40,50,60,70]
#part4
List1.append(40)

print("List1 : ",List1,"\n")
#part5
List2 = List2 + List1
print("List2 : ",List2,"\n")
#part6
List2 = list(set(List2))

print("List2 after removing duplicates : ",List2)
