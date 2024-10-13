library(arules)
dataset=read.transactions("C:/Users/DELL/Desktop/SEM-6/DM/AssociationRuleMining/X1000_Out.csv",sep=",",rm.duplicate=TRUE)
dataset

summary(dataset)

itemFrequencyPlot(dataset,topN=10)

#a) Use minimum support as 50% and minimum confidence as 75% 
rules=apriori(data=X1000_Out,parameter = list(support=0.5,confidence=0.75))
rules 
inspect(rules[1:100])
inspect(sort(rules,by="confidence")[1:20])

#b) Use minimum support as 60% and minimum confidence as 60%
rules=apriori(data=X1000_Out,parameter = list(support=0.6,confidence=0.6))
rules
inspect(rules[1:100])
inspect(sort(rules,by="confidence")[1:20])

#c) Use different support and confidence thresholds.
rules=apriori(data=X1000_Out,parameter=list(support=0.005,confidence=0.6))
rules
inspect(rules[1:100])
inspect(sort(rules,by="confidence")[1:20])
