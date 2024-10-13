def ispangram(string):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in string.lower():
         return False
   return True

string=input("Enter a string : ")
if(ispangram(string) == True):
   print("The string is a pangram")
else:
   print("The string is not a pangram")
