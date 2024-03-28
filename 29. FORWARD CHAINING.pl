% Define facts and rules
fact(has_fur, dog).
fact(has_tail, dog).
fact(has_fur, cat).
fact(has_tail, cat).
fact(has_feathers, bird).

rule(mammal, X) :-
    fact(has_fur, X),
    fact(has_tail, X).
rule(animals, X) :-
    fact(has_fur, X).
rule(animals, X) :-
    fact(has_feathers, X).

% Derived facts
:- dynamic(derived/1).
derived([]).

% Implement forward chaining
forward_chaining :-
    derived(Derived),
    rule(Consequent, X),
    \+ member(Consequent, Derived), % Check if already derived
    \+ fact(Consequent, X), % Check if not already known as a fact
    check_conditions(X, Consequent, [Consequent | Derived], NewDerived),
    update_derived(NewDerived),
    forward_chaining.

% Update derived facts
update_derived(NewDerived) :-
    retract(derived(_)),
    assertz(derived(NewDerived)).

% Check if all conditions of a rule are satisfied
check_conditions(_, X, Derived, Derived) :-
    fact(X, _). % Base case: X is already a fact

check_conditions(X, X, Derived, Derived). % Base case: Consequent is the same as the target

check_conditions(Target, Consequent, Derived, NewDerived) :-
    rule(Consequent, Target), % Check if Consequent depends on Target
    \+ member(Consequent, Derived), % Check if already derived
    \+ fact(Consequent, _), % Check if not already known as a fact
    check_conditions(Target, Consequent, [Consequent | Derived], NewDerived). % Continue checking conditions

% Entry point
start_forward_chaining :-
    forward_chaining.
