conc([],L1,L1).
conc([X|T],L2,[X|T1]):- conc(T,L2,T1).
