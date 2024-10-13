library(editrules)

df=read.csv("employee.txt")
r=editfile("r2.txt")
ve=violatedEdits(r,df)

summary(ve)
plot(ve)
 