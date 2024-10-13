#Function with deafult arguments
ofunc <-function(a=20, b=50)
{fres <-a*b
print(fres)
}

ofunc() #Calling with default arguments
ofunc(14,50) #Changing the default arguments

#Function with multiple arguments
named <- function(p,q,r,s)
{r1 <- p*q
r2 <-r-s
r3<- r1+r2
print (r3)}

#Function call with same order of arguments
named(7,8,9,2)

#Function call with different order of arguments, by name
x <-named(r=9,p=7,s=2, q=8)
x
