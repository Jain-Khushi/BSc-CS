library(editrules)
p1<-read.csv("employee.txt")
e <-editfile("editrules.txt")
e
ve <- violatedEdits(e,p1)
summary(ve)
plot(ve)

