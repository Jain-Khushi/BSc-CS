# Question-1
# Load the dataset
data("cars")

# Display the structure of the dataset
str(cars)

# Compute the mean, geometric mean, harmonic mean, and median of speed and dist columns
speed_mean <- mean(cars$speed)
print(speed_mean)
speed_gmean <- exp(mean(log(cars$speed)))
print(speed_gmean)
speed_hmean <- length(cars$speed) / sum(1/cars$speed)
print(speed_hmean)
speed_median <- median(cars$speed)
print(speed_median)

dist_mean <- mean(cars$dist)
print(dist_mean)
dist_gmean <- exp(mean(log(cars$dist)))
print(dist_gmean)
dist_hmean <- length(cars$dist) / sum(1/cars$dist)
print(dist_hmean)
dist_median <- median(cars$dist)
print(dist_median)

# Find the unique values of dist column
dist_unique <- unique(cars$dist)
print(dist_unique)

# Find the variance of both the columns
speed_var <- var(cars$speed)
print(speed_var)
dist_var <- var(cars$dist)
print(dist_var)

# Find the IQR of speed column
speed_IQR <- IQR(cars$speed)
print(speed_IQR)

# Create quartiles for dist column
dist_quartiles <- quantile(cars$dist, probs = c(0.25, 0.5, 0.75))
print(dist_quartiles)




# Question-2
# Load the dataset
dirty_android1 <- read.csv("C:/Users/DELL/Desktop/SEM-6/DM/R Practicals/Dirty android1 data.csv", header=FALSE)
View(dirty_android1)

# Identify the count of NA's in the data frame
na_count <- sum(is.na(dirty_android1))
print(na_count)

# Calculate the number and percentage of observations that are complete
complete_observations <- sum(complete.cases(dirty_android1))
print(complete_observations)
complete_percentage <- complete_observations/nrow(dirty_android1) * 100
print(complete_percentage)

# Find the position of NA values in LCOM3 column
na_index <- which(is.na(dirty_android1$LCOM3))
print(na_index)

# Report the mean values of each column
column_means <- colMeans(dirty_android1, na.rm = TRUE)
print(column_means)

# Replace all empty rows with mean values of the column
dirty_android1[is.na(dirty_android1)] <- lapply(dirty_android1, function(x) ifelse(is.na(x), mean(x, na.rm = TRUE), x))
print(dirty_android1[is.na(dirty_android1)])

# Report the mean values of each column after replacing empty rows with mean values
column_means_after_replacement <- colMeans(dirty_android1)
print(column_means_after_replacement)

# Read the dataset again in another data frame variable and omit all the records with NA values
dirty_android1_omitted <- dirty_android1[complete.cases(dirty_android1),]
print(dirty_android1_omitted)
