# Load libraries
library(klaR)
library(e1071)

BreastCancer <- read.csv("C:/Users/DELL/Desktop/SEM-6/DM/CP_DifferentValidation/BreastCancer.csv")
# BreastCancer<-BreastCancer1[,-2]
data("BreastCancer", package = "mlbench")
data <- data.frame(BreastCancer)

set.seed(123)
train_index <- sample(nrow(data), round(0.75 * nrow(data)), replace = FALSE)
train_set <- data[train_index, ]
test_set <- data[-train_index, ]

train_set[, 2:10] <- scale(train_set[, 2:10])
test_set[, 2:10] <- scale(test_set[, 2:10])

# KNN without standardizing attributes
knn_model1 <- train.kknn(diagnosis ~ ., data = train_set, kernel = "rectangular", k = 5)
# KNN after standardizing attributes
knn_model2 <- train.kknn(diagnosis ~ ., data = train_set, kernel = "rectangular", k = 5, scale = TRUE)
# Naive Bayes
nb_model <- naiveBayes(diagnosis ~ ., data = train_set)

# Holdout validation
knn1_holdout_acc <- sum(predict(knn_model1, test_set) == test_set$diagnosis) / nrow(test_set)
knn2_holdout_acc <- sum(predict(knn_model2, test_set) == test_set$diagnosis) / nrow(test_set)
nb_holdout_acc <- sum(predict(nb_model, test_set) == test_set$diagnosis) / nrow(test_set)

# Bootstrap validation
knn1_bootstrap_acc <- boot::boot(train_set, function(data, index) {
  train <- data[index, ]
  test <- data[-index, ]
  model <- train.kknn(diagnosis ~ ., data = train, kernel = "rectangular", k = 5)
  pred <- predict(model, test)
  sum(pred == test$diagnosis) / nrow(test)
}, R = 100)$t

knn2_bootstrap_acc <- boot::boot(train_set, function(data, index) {
  train <- data[index, ]
  test <- data[-index, ]
  model <- train.kknn(diagnosis ~ ., data = train, kernel = "rectangular", k = 5, scale = TRUE)
  pred <- predict(model, test)
  sum(pred == test$diagnosis) / nrow(test)
}, R = 100)$t

nb_bootstrap_acc <- boot::boot(train_set, function(data, index) {
  train <- data[index, ]
  test <- data[-index, ]
  model <- naiveBayes(diagnosis ~ ., data = train)
  pred <- predict(model, test)
  sum(pred == test$diagnosis) / nrow(test)
}, R = 100)$t

# LOOCV validation
knn1_loocv_acc <- sum(predict(knn_model1, train_set, type = "class") == train_set$diagnosis) / nrow(train_set)
knn2_loocv_acc <- sum(predict(knn_model2, train_set, type = "class") == train_set$diagnosis)

knn1_loocv_acc <- sum(predict(knn_model1, train_set, type = "class") == train_set$diagnosis) / nrow(train_set)
knn2_loocv_acc <- sum(predict(knn_model2, train_set, type = "class") == train_set$diagnosis) / nrow(train_set)
nb_loocv_acc <- sum(predict(nb_model, train_set, type = "class") == train_set$diagnosis) / nrow(train_set)

# K-fold cross validation
k_fold <- function(data, k, model_func, ...) {
  indices <- sample(rep(1:k, length.out = nrow(data)))
  fold_acc <- numeric(k)
  for (i in 1:k) {
    train <- data[indices != i, ]
    test <- data[indices == i, ]
    model <- model_func(train, ...)
    pred <- predict(model, test)
    fold_acc[i] <- sum(pred == test$diagnosis) / nrow(test)
  }
  return(mean(fold_acc))
}

# 5-fold cross validation
knn1_5fold_acc <- k_fold(train_set, 5, train.kknn, kernel = "rectangular", k = 5)
knn2_5fold_acc <- k_fold(train_set, 5, train.kknn, kernel = "rectangular", k = 5, scale = TRUE)
nb_5fold_acc <- k_fold(train_set, 5, naiveBayes)

# 10-fold cross validation
knn1_10fold_acc <- k_fold(train_set, 10, train.kknn, kernel = "rectangular", k = 5)
knn2_10fold_acc <- k_fold(train_set, 10, train.kknn, kernel = "rectangular", k = 5, scale = TRUE)
nb_10fold_acc <- k_fold(train_set, 10, naiveBayes)

# 20-fold cross validation
knn1_20fold_acc <- k_fold(train_set, 20, train.kknn, kernel = "rectangular", k = 5)
knn2_20fold_acc <- k_fold(train_set, 20, train.kknn, kernel = "rectangular", k = 5, scale = TRUE)
nb_20fold_acc <- k_fold(train_set, 20, naiveBayes)

# Repeated k-fold cross validation
repeated_k_fold <- function(data, k, repeats, model_func, ...) {
  repeat_acc <- numeric(repeats)
  for (i in 1:repeats) {
    repeat_acc[i] <- k_fold(data, k, model_func, ...)
  }
  return(mean(repeat_acc))
}

# 5-repeated 5-fold cross validation
knn1_5repeats_5fold_acc <- repeated_k_fold(train_set, 5, 5, train.kknn, kernel = "rectangular", k = 5)
knn2_5repeats_5fold_acc <- repeated_k_fold(train_set, 5, 5, train.kknn, kernel = "rectangular", k = 5, scale = TRUE)
nb_5repeats_5fold_acc <- repeated_k_fold(train_set, 5, 5, naiveBayes)

# 10-repeated 5-fold cross validation
knn1_10repeats_5fold_acc <- repeated_k_fold(train_set, 5, 10, train.kknn, kernel = "rectangular", k = 5)
knn2_10repeats_5fold_acc <- repeated_k_fold(train_set, 5, 10, train.kknn, kernel = "rectangular", k = 5, scale = TRUE)
nb_10repeats_5fold_acc <- repeated_k_fold(train_set, 5, 10, naiveBayes)

# 20-repeated 5-fold cross validation
knn1_20repeats_5fold_acc <- repeated_k_fold(train_set, 5, 20, train.kknn, kernel = "rectangular", k = 5)
knn2_20repeats_5fold_acc <- repeated_k_fold(train_set, 5, 20, train.kknn, kernel = "rectangular", k = 5, scale = TRUE)
nb_20repeats_5fold_acc <- repeated_k_fold(train_set, 5, 20, naiveBayes)

# Store results in a data frame
results <- data.frame(Method = c("Holdout", "Bootstrap", "LOOCV", "5-Fold", "10-Fold", "20-Fold", "5-Repeats of 5-Fold", "10-Repeats of 5-Fold", "20-Repeats of 5-Fold"),
                      KNN1 = c(knn1_holdout_acc, knn1_bootstrap_acc, knn1_loocv_acc, knn1_5fold_acc, knn1_10fold_acc, knn1_20fold_acc, knn1_5repeats_5fold_acc, knn1_10repeats_5fold_acc, knn1_20repeats_5fold_acc),
                      KNN2 = c(knn2_holdout_acc, knn2_bootstrap_acc, knn2_loocv_acc, knn2_5fold_acc, knn2_10fold_acc, knn2_20fold_acc, knn2_5repeats_5fold_acc, knn2_10repeats_5fold_acc, knn2_20repeats_5fold_acc),
                      NB = c(nb_holdout_acc, nb_bootstrap_acc, nb_loocv_acc, nb_5fold_acc, nb_10fold_acc, nb_20fold_acc, nb_5repeats_5fold_acc, nb_10repeats_5fold_acc, nb_20repeats_5fold_acc))

# Create plot
library(ggplot2)
library(reshape2)
results_melted <- melt(results, id.vars = "Method")
ggplot(results_melted, aes(x = Method, y = value, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(x = "Validation Method", y = "Accuracy", fill = "Classifier") +
  ggtitle("Accuracy of Classification Models using Different Validation Methods") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5),
        axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

# Display plot
print(ggplot(results_melted, aes(x = Method, y = value, fill = variable)) +
        geom_bar(stat = "identity", position = "dodge") +
        labs(x = "Validation Method", y = "Accuracy", fill = "Classifier") +
        ggtitle("Accuracy of Classification Models using Different Validation Methods") +
        theme_bw() +
        theme(plot.title = element_text(hjust = 0.5),
              axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)))


