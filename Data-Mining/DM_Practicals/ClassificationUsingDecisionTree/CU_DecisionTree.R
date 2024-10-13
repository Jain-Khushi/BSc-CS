iris1 <- read.csv("C:/Users/DELL/Desktop/SEM-6/DM/ClassificationUsingDecisionTree/iris_dirty.csv")
iris<-subset(iris,select=-c(Species))

# Load the RWeka library
library(RWeka)

# Load the iris dataset
data(iris)

# Split the data into training and testing sets
set.seed(123)
train_index <- sample(1:nrow(iris), round(0.75 * nrow(iris)))
train_data <- iris[train_index, ]
test_data <- iris[-train_index, ]

# Build the decision tree classifier using J48 algorithm
j48_model <- J48(Species ~ ., data = train_data)

# Use the classifier to predict the species of the test data
predictions <- predict(j48_model, newdata = test_data)

# Print the confusion matrix and overall accuracy of the classifier
library(caret)
confusionMatrix(predictions, test_data$Species)
