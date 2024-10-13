sum <- function(a,b)
{
  result <- a+b
  print(result)
}
sub<- function(a,b)
{
  result <- a-b
  print(result)
}

mult <- function(a,b)
{
  result <- a*b
  print(result)
}

div <-function (a,b)
{
  result <-a/b
  print (result)
}

x1<-5
x2<-6
print ("Enter you choice")
ans2 = scan()

if (ans2==1)
{
  sum(x1,x2)
}else if (ans2 ==2)
      {
      sub(x1,x2)
}else if (ans2 ==3)
  {
    mult(x1,x2)
  }else
{
  div(x1, x2)
}
