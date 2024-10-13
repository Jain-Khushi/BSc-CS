def change(str):
  char = str[0]
  str = str.replace(char, '@')
  str = char + str[1:]

  print("Result :",str)

str=input("Enter a string : ")
change(str)
