# Question 1

v = c(1, 2, NULL, 3, 4, NULL)
print("Original vector:")
print(v)
new_v = (v+7)[(!is.na(v)) & v > 0]
print("New vector:")
print(new_v)

# Question 2

v = c(15,70,99,71,10,0,9,55)
print("Original vector:")
print(v)
print("Test whether the value > 65 or not:")
print(v > 65)

# Question 3

v = sample(-50:50, 10, replace=TRUE)
print("Content of the vector:")
print("10 random integer values between -50 and +50:")
print(v)

# Question 4

x <- c(1, 2, 3, 4, 5, 6)             
y <- c(7, 2, 8, 9, 5, 9, 5)
print("Union is : ")
union(x,y)
print("Intersection is : ")
intersect(x,y)
print("Set Difference is :")
setdiff(x,y)

# Question 5

#(a)
a <-c(1:4,13,rep(c(2,-5.1,-23),3),sum((7/42),3,(35/42)))
a

#(b)
sort(a,decreasing=FALSE)
L <-length(sort(a,decreasing=FALSE))
L
sort(seq(from = L, to = 1),decreasing = TRUE)
addition <- (sort(seq(from = L, to = 1),decreasing = TRUE)) + (sort(a,decreasing=FALSE))

# Question 6

my_list = list(Chr="Python", nums = 1:15, flag=TRUE)
print(my_list)

# Question 7

a<-c(1,2,3)
b<-c(4,5,6)
c<-c(7,8,9)
m<-cbind(a,b,c)
print("Content of the said matrix:")
print(m)

# Question 8

Newlist <- list(a=1:10, b="Good morning", c="Hi")
Newlist$a = Newlist$a +1
Newlist$a

# Question 9

x <- list(a=5:10, c="Hello", d="AA")
x$z <- "NewItem"
x

# Question 10

y <- list("a", "b", "c")
names(y) <- c("one","two","three")
y

# Question 11

data <- c(7, 2, 9, 4, 12, 13)
A <- matrix(data, nrow = 2, ncol = 3)

data <- c(1, 2, 3, 7, 8, 9, 12, 13, 14, 19, 20, 21)
B <- matrix(data, nrow = 3, ncol = 4)

AB <- A %*% B

print("Matrix A")
print(A)
print("Matrix B")
print(B)
print("Matrix Multiplication Result")
print(AB)


# Question 12

binary_search <- function(vec, key) {
  # Sort the vector
  vec <- sort(vec)
  # Get the length of the vector
  n <- length(vec)
  # Set the start and end index for the search
  start <- 1
  end <- n
  
  # Continue the search as long as start <= end
  while (start <= end) {
    # Get the middle index
    mid <- floor((start + end) / 2)
    # If the key is found at the middle, return the index
    if (vec[mid] == key) {
      return(mid)
    } 
    # If the key is greater than the middle value, search in the right half
    else if (vec[mid] < key) {
      start <- mid + 1
    } 
    # If the key is smaller than the middle value, search in the left half
    else {
      end <- mid - 1
    }
  }
  
  # Return -1 if the key is not found
  return(-1)
}

# Test the binary_search function
vec <- c(1, 12, 23, 34, 56, 99)
cat("Vectors:",vec)
key <- as.integer(readline(prompt = "Enter number:"))
result <- binary_search(vec, key)
cat("Result:", result, "\n")

# Question 13

a <- array(seq(from = 50, length.out = 15, by = 2), c(5, 3))
print("Content of the array:")
print("5×3 array of sequence of even integers greater than 50:")
print(a)

# Question 14

mons_v = c("March","April","January","November","January",
           "September","October","September","November","August","February",
           "January","November","November","February","May","August","February",
           "July","December","August","August","September","November","September",
           "February","April")
print("Original vector:")
print(mons_v)
f = factor(mons_v)
print("Ordered factors of the said vector:")
print(f)
print(table(f))

# Question 15

A <- rbind(c(1, -2, 3), 
           c(2, 1, 1), 
           c(-3, 2, -2))
B <- c(7, 4, -10)

# Solve them using solve function in R
solve(A, B)

# Question 16

dim <- as.integer(readline(prompt="Enter the dimensions of the matrix: "))

mat <- matrix(nrow=dim, ncol=dim)
for (i in 1:dim) {
  for (j in 1:dim) {
    mat[i,j] <- as.numeric(readline(prompt=paste0("Enter the value of (", i, ",", j, "): ")))
  }
}

# Check if the matrix is symmetric
if (all(mat == t(mat))) {
  print("The matrix is symmetric.")
} else {
  print("The matrix is not symmetric.")
}

# Question 17

#(i)
x<- c(0,1,1,2,3,5,8,13,21,34,NA,11,NA)
result.mean <-  mean(x,na.rm = TRUE)
print(result.mean)
result.median <- median(x,na.rm = TRUE)
print(result.median)

#(ii)
matrix_sq <- matrix(data=1:9, nrow=3, ncol=3, byrow=TRUE)^2
print("Matrix of square of 1st nine natural numbers:")
print(matrix_sq)

#(iii)
ata <- c(1, 2, 7, 2, 8, 4, 3, 0, 9)
A <- matrix(data, nrow = 3, ncol = 3)
A_T <- t(A)
print("Matrix A")
print(A)
print("Transpose of A")
print(A_T)

#(iv)
data <- c(1,2,3,4,5,6,7,8,9)
A <- matrix(data, nrow = 3, ncol = 3)
data <- c(1,2,3,4,5,6,7,8,9)
B <- matrix(data, nrow = 3, ncol = 3)
print("Matrix A: ")
print(A)
print("Matrix B : ")
print(B)
print("Matrix Multiplication : ")
print(A %*% B)

#(v)
mylist1 <- list("cherry", 'banana') 
mylist2 <- list(1, 2, 3, 4, 5)
jointlist <- c(mylist1, mylist2)
jointlist

#(vi)
vector <- 1:10
for(i in vector){
  if(i %% 2 == 0){
    print(i)
  }
}

#(vii)
vector <- c(3, 5, 1, 10, 8, 2)
sorted_vector <- sort(vector)
print("Sorted vector in ascending order:")
print(sorted_vector)

