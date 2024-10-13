i <- 14

if (i<20)
{
  print("i is less than 20")
  if (i<10)
    {
      print("i is also less than 10")
    }else
    {
      print("i is greater than 10 but less than 20")
    }
}

sales <- 250
if (sales>200 && sales<500)
  { 
  print("Normal Sales")
}else{
  print("Check the figures")  
}

if (sales>500 || sales<200)
{ 
  print("Extreme Sales")
}else{
  print("Average Sales")  
}
