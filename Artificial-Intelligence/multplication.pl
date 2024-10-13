mul(N,1,N).
mul(N,M,A):-
T is M-1,
mul(N,T,Y),
A is Y+N.
