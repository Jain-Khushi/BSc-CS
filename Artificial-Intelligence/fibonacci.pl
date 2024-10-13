input:-write("Enter the Nth term of fibonacci series : "),read(N),fib(N,T),write(T).
fib(0,0).
fib(1,1).
fib(N,T):-N1 is N-1,fib(N1,T1),N2 is N-2,fib(N2,T2),T is T1+T2.
