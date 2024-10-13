max([H],H).
max([H|T],R):-
 max(T,M1),
 H>=M1,
 R is H,!.
max([H|T],R):-
 max(T,M1),
 H<M1,
 R is M1.
