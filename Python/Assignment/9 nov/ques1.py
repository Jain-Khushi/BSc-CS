def ISBN_10(str1):
    j=10
    result=0
    for i in str1:
        if(i=='-'):
            continue
        if(j>0):
            result=result+int(i)*j
            j=j-1
    result=result % 11

    return result


s1=input('Enter the string: ')
if(ISBN_10(s1)==0):
    print('This is a valid ISBN-10')
else:
    print('This is NOT valid ISBN-10')
