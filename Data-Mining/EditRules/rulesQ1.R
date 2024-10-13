library(editrules)
p1<-read.csv("people.txt")
e <-editfile("edit.txt")
e
ve <- violatedEdits(e,p1)
summary(ve)
plot(ve)
