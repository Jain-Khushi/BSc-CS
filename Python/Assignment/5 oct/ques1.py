MyString = 'Computer Education'
print("Original string :",MyString)
print()

string1=MyString[13:]
print("(a) Displaying the last five characters : ",string1)

string2=MyString[::-1]
print("(b) Displaying the string in reverse order :",string2)

string3=MyString.partition('put')
print("(c) Searching for a substring ‘put’,and splitting the string into a tuple containing three elements :",string3)

string4=MyString.count('o',0,8)
print("(d) Counting no. of times letter ‘o’ appeared in MyString(excluding its appearance in the word ‘Education’ :",string4)

string5=MyString.swapcase()
print("(e) Displaying the string in Toggle Case :",string5)

string6=MyString.replace('u','#*')
print("(f) Replacing all the occurrences of letter “u” in the string with “#*” :",string6)
