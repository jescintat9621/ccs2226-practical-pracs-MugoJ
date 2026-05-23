%section 1-part A:ready made family tree

% Facts to support the practical exercises
parent(carmel, dan).
parent(carmel, david).
parent(carmel, stacy).
parent(steve, dan).
parent(steve, david).
parent(steve, stacy).

parent(david, daniel).
parent(david, giana).

parent(pat, carmel).
parent(mary, carmel).
parent(pat, john).
parent(mary, john).

married_to(carmel, steve).
married_to(steve, carmel).

male(steve).
male(dan).
male(david).
male(daniel).
male(pat).
male(john).

female(carmel).
female(stacy).
female(giana).
female(mary).

%part B:running the file to find children or spouses
?- consult('family.pl').

% Find all children of carmel (Press ';' to cycle through outcomes)
?- parent(carmel, X).
% Output: X = dan ; X = david ; X = stacy.

% Find carmel's husband
?- married_to(carmel, X).
% Output: X = steve.

%part C:Rules for parents based on gender
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).

%code tesying:
?- father(X, dan).
% Output: X = steve.

?- mother(X, dan).
% Output: X = carmel.

% Rule to check if X and Y are distinct entities
diff(X, Y) :- X \== Y.

%part F:Defining advanced relationship predicates
% Helper difference rule
diff(X, Y) :- X \== Y.

% 1. Sibling: Share at least one parent and are not the same person
sibling(X, Y) :- parent(Z, X), parent(Z, Y), diff(X, Y).

% 2. Brother: Is a sibling and male
brother(X, Y) :- sibling(X, Y), male(X).

% 3. Sister: Is a sibling and female
sister(X, Y) :- sibling(X, Y), female(X).

% 4. Grandparent
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% 5. Grandmother
grandmother(X, Y) :- grandparent(X, Y), female(X).

% 6. Grandfather
grandfather(X, Y) :- grandparent(X, Y), male(X).

% 7. Blood Uncle (bl_uncle): Brother of a parent
bl_uncle(X, Y) :- parent(Z, Y), brother(X, Z).

% 8. Uncle in-law: Married to a blood aunt (sister of a parent)
uncle_in_law(X, Y) :- parent(Z, Y), sister(W, Z), married_to(X, W), male(X).

% 9. Uncle: Any type of uncle (blood or by marriage)
uncle(X, Y) :- bl_uncle(X, Y).
uncle(X, Y) :- uncle_in_law(X, Y).

%part G:Davids relationship
% David's siblings
?- sibling(X, david).
% Output: X = dan ; X = stacy.

%David's grandparents
?- grandparent(X, david).
% Output: X = pat ; X = mary.

%part H:task box rules
% Aunt: Sister of a parent, or married to a blood uncle
aunt(X, Y) :- parent(Z, Y), sister(X, Z).
aunt(X, Y) :- parent(Z, Y), bl_uncle(W, Z), married_to(X, W), female(X).

% First Cousin: Share a common grandparent but are not siblings or the same person
firstcousin(X, Y) :- grandparent(Z, X), grandparent(Z, Y), \+ sibling(X, Y), diff(X, Y).

% Ancestor (Recursive definition)
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Descendant (Inverse of ancestor)
descendant(X, Y) :- ancestor(Y, X).

%sample input and output
?- firstcousin(daniel, X).
% Output: false (No cousins defined in current dataset)

?- ancestor(pat, daniel).
% Output: true.

?- descendant(daniel, pat).
% Output: true.


%Section 2-Syntax implementation example
% (b) Operator Definitions
:- op(700, xfy, are).
:- op(600, fx, the).
:- op(500, fx, sisters).
:- op(500, fx, brothers).
:- op(400, fx, of).

% (a) Base listing predicate using setof/3
sister_list(X, L) :- setof(Y, sister(Y, X), L).
brother_list(X, L) :- setof(Y, brother(Y, X), L).

% (c) Mapping the natural language phrase to the logic logic engine
Who are the sisters of X :- sister_list(X, Who).

% (e) Adding code for brothers
Who are the brothers of X :- brother_list(X, Who).

% (f) Alternative phrasing operator rule
Give me the brothers of X :- brother_list(X, Who).


%Section3-testing natural queries
?- Who are the sisters of daniel.
% Output: Who = [giana].

?- Who are the brothers of daniel.
% Output: false. (Since daniel only has a sister)

?- Who are the brothers of david.
% Output: Who = [dan].

?- Give me the brothers of david.
% Output: Who = [dan].



