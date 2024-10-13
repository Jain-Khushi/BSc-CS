# Menu driven program to perform operations on strings:

def length():
    s=input("\nEnter the string : ")
    print("Length of string is:",len(s))

def maximum():
    s1=input("\nEnter string 1 : ")
    s2=input("Enter string 2 : ")
    s3=input("Enter string 3 : ")
    if s1>s2:
        if s1>s3:
            print("Maximum string :",s1)
        else:
            print("Maximum string :",s3)
    elif s2>s3:
        print("Maximum string :",s2)
    else:
        print("Maximum string is :",s3)

def replace():
    s=input("\nEnter a string : ")
    k="#"
    vowels='AEIOUaeiou'
    for i in vowels:
        s=s.replace(i,k)
    print("New string is :",s)

def words():
    s= input("\nEnter a string : ")
    s1=s.split();
    l=len(s1)
    print("Number of words :",l)

def palindrome():
    s=input("\nEnter a string : ")
    string=""
    for i in s:
        string = i+string

    if (s == string):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
        
        
while True:
    print("\n    Operations on strings    \n")
    print("1. Find the length of string")
    print("2. Return maximum of three strings")
    print("3. Accept a string and replace all vowels with “#” ")
    print("4. Find number of words in the given string")
    print("5. Check whether the string is a palindrome or not")
    print("6. Exit")
    choice=int(input("Enter your choice : "))

    if choice==1:
        length()
    elif choice==2:
        maximum()
    elif choice==3:
        replace()
    elif choice==4:
        words()
    elif choice==5:
        palindrome()
    elif choice==6:
        break
    else:
        print("Wrong choice!!")
        break
    

