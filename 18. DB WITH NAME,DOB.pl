% Database of individuals with names and DOBs
person(john, '1990-05-15').
person(susan, '1985-11-30').
person(michael, '1995-02-10').
person(emily, '2000-08-22').

% Predicate to retrieve the DOB of a person
get_dob(Name, DOB) :-
    person(Name, DOB).

