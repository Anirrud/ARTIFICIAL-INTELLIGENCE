% Facts about the graph's edges and their costs
edge(a, b, 2).
edge(a, c, 5).
edge(b, d, 3).
edge(c, e, 4).
edge(d, g, 1).
edge(e, g, 7).

% Best First Search algorithm
best_first_search(Start, Goal) :-
    empty_priority_queue(EmptyQueue),
    add_to_queue(Start, EmptyQueue, Queue),
    search(Goal, Queue).

search(Goal, [(Goal, _) | _]) :- % Goal found
    format('Goal ~w found.~n', [Goal]).

search(Goal, [(Node, _) | RestQueue]) :-
    findall(Child, edge(Node, Child, _), Children),
    add_list_to_queue(Children, RestQueue, NewQueue),
    search(Goal, NewQueue).

% Priority queue implementation
empty_priority_queue([]).

add_to_queue(Node, Queue, NewQueue) :-
    heuristic(Node, H),
    insert_queue(Node, H, Queue, NewQueue).

add_list_to_queue([], Queue, Queue).
add_list_to_queue([Node | RestNodes], Queue, NewQueue) :-
    add_to_queue(Node, Queue, TempQueue),
    add_list_to_queue(RestNodes, TempQueue, NewQueue).

insert_queue(Node, H, [], [(Node, H)]).

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node, H), (Node2, H2) | RestQueue]) :-
    H =< H2.

insert_queue(Node, H, [(Node2, H2) | RestQueue], [(Node2, H2) | NewRestQueue]) :-
    H > H2,
    insert_queue(Node, H, RestQueue, NewRestQueue).

% Heuristic function (dummy, you can replace this with real heuristics)
heuristic(_, 0).

