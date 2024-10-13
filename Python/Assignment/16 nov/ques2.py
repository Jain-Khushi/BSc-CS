num=int(input("Enter the number : "))
num_b="{0:b}".format(num)
print(num_b)
num_r=str(num_b)[::-1]
print(num_r)
if num_r==num_b:
    print("The binary representaion of the number is palindrome.")
else:
    print("The binary representaion of the number is not palindrome.")
