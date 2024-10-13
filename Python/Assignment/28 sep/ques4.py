s=input("Enter a string : ")
sum = 0
digit = ""

for i in s :
    if i.isdigit() :
        sum += int(i)
        digit = digit + " " +i
        
if sum == 0 :
    print("The string has no digits.")
else :
    print("\nOriginal string : ", s)
    print("Digits are: ", digit)
    print("Sum of all digits : ", sum)
