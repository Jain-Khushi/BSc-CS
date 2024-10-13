#Program to find whether a string entered by the user is a palindrome or not.

word=input("Enter a string : ")
string=""
for i in word:
    string = i+string
print("Reverse of the string :",string)

if (word == string):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
    
