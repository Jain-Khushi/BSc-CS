rev([],Y,R):-R=Y.
rev([H|T],Y,R):-rev(T,[H|Y],R).
