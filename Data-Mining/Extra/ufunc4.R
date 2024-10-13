#using return to output function from a user defined function
outfunc <-function(a,b)
  return (a*b)


outfunc(7,5)

#output given from the function is stored in a variable
ans <- outfunc(9,8)
ans

#Passing unequal number of arguments
outfunc(a=10)

