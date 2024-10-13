library(editrules)

df=read.csv("people.txt")

r=editfile("r1.txt")

ve=violatedEdits(r,df)
summary(ve)
plot(ve)
