% Facts: parent(Parent, Child)
parent(steve, john).
parent(steve, alison).
parent(mercy, john).
parent(mercy, alison).

parent(john, patrick).
parent(john, vivian).
parent(ann, patrick).
parent(ann, vivian).

parent(alison, paul).
parent(david, paul).

% Gender facts
male(steve).
male(john).
male(david).
male(patrick).
male(paul).

female(mercy).
female(alison).
female(ann).
female(vivian).

% Rules
diff(X, Y) :- X \== Y.

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    diff(X, Y).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandchild(X, Y) :-
    grandparent(Y, X).

uncle(X, Y) :-
    male(X),
    sibling(X, Z),
    parent(Z, Y).

aunt(X, Y) :-
    female(X),
    sibling(X, Z),
    parent(Z, Y).

cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    sibling(P1, P2).