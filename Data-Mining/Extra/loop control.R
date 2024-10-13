for (i in 11:20)
  {
  print (i)
  if (i>15)
  {
    break
  }
}


alphabet <- LETTERS[1:7]
for (i in alphabet)
{ 
  if (i=="C")
  {
    next
  }
print(i)
}
