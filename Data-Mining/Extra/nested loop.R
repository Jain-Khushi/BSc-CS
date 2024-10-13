x <-matrix(1:12,4,3)

for (i in seq_len(nrow(x))) {
  for (j in seq_len(ncol(x))){
    print(x[i,j])
  }
}