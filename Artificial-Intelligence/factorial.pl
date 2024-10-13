fact(0,1).
fact(1,1).
fact(N,R):-X is N-1,fact(X,Y),R is Y*N.
