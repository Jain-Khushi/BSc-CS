# For wine dataset
wine <- read.csv(wine <- read.csv("C:/Users/DELL/Desktop/SEM-6/DM/PL_Q3/wine.csv", header=FALSE))
wine

# Hierarchical Clustering
id1 <- sample(1:dim(wine)[1],30)
id1

wineSample <- wine[id1,]
wineSample$Species <- NULL
wineSample

hc <- hclust(dist(wineSample),method="ave")

plot(hc,hang=-1,labels=wine$Species[id1])

rect.hclust(hc,k=4)

groups <- cutree(hc,k=4)

# DBSCAN Practical
library(fpc)
#wine1<-read.transactions("C:/Users/DELL/Desktop/SEM-6/DM/PL_Q3/wine.csv",sep=",",rm.duplicate=TRUE)
#wine1
#data(wine1)
wine2 <- wine[-5]
wine2
ds <- dbscan(wine2,eps=0.45,MinPts=5)
ds
str(ds)
ds$cluster
table(ds$cluster,wine$Species)
plot(ds,wine2[c(1,4)])
plot(ds,wine2)

