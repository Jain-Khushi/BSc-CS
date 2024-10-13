# WINE DATASET
wine <- read.csv("C:/Users/DELL/Desktop/SEM-6/DM/PL_Q3/wine.csv", header=FALSE)
wine

# Check if the attributes are standardized
apply(wine, 2, mean)   # should return a vector of zeros
apply(wine, 2, sd)     # should return a vector of ones

# Standardize the wine attributes
wine <- scale(wine)
wine

# IRIS DATASET
iris <- read.csv("C:/Users/DELL/Desktop/SEM-6/DM/PL_Q3/iris_dirty.csv")
iris1<-subset(iris,select=-c(Species))
# Check if the attributes are standardized
apply(iris1, 2, mean)   # should return a vector of non-zero values
apply(iris1, 2, sd)     # should return a vector of non-one values

# Standardize the iris attributes
iris1 <- scale(iris1)
iris1
