#Function with single argument
mfunc <-function(arg1)
{for (i in 1:arg1)
  {result <- i *3
  print (result)}
}

mfunc(9)

#Function with multiple arguments
newfunc <- function(a,b,c,d)
{res <- a*b+c-d
print (res)}

newfunc(7,8,9,2)
