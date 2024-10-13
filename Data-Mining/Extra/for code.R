#Using range in for loop
for (i in 2:7)
  {
  print(i^2)
  }

#Using for loop for numeric vector
for (i in c(5,7,9, 11,13))
  {
  print(i^3)
  }


#Using for loop for displaying from predefined term letters
x <- letters
for (i in 1:4)
  print (x[i])

#Using for loop for displaying from predefined term LETTERS
alphabet <- LETTERS[2:6]
for ( i in alphabet)
{
  print(i)
}
