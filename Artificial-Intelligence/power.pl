power(0,_P,0).
power(_X,0,1).
power(X,P,A):- P1 is P-1,
power(X,P1,Ans),
A is Ans*X.
