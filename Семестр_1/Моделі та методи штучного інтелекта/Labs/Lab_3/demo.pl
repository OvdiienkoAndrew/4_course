:- dynamic city/4.

node(a,b,40).
node(b,a,40).

node(a,c,10).
node(c,a,10).

node(c,b,30).
node(b,c,30).

node(c,d,100).
node(d,c,100).

node(d,b,50).
node(b,d,50).

start:-
    retractall(city(_,_,_,_)),
    forall(node(X, Y, _), (
        (city(X, _, _, _) -> true ; assertz(city(X, 1000000000, 0, none))),
        (city(Y, _, _, _) -> true; assertz(city(Y, 1000000000, 0, none)))
    )).


find_way(A, B, Size) :-
    start,
    
    retract(city(A, _, _, _)),
    assertz(city(A, 0, 0, none)),

    dijkstra,

    city(B, Size, _, _).


dijkstra :-
    setof(Point-City, city(City, Point, 0, _), Unsorted),
    (Unsorted = [] -> 
        writeln('Finish.')
    ;
     writeln('Start.')
        Unsorted = [_-MinNode|_],
        writeln(Unsorted)

        cost(MinNode),
        visited(MinNode),
        dijkstra
    ).

cost(A) :-
    city(A, OldCost, _, _),
    forall(node(A, B, EdgeCost),
        (
            New_Cost is OldCost + EdgeCost,
            city(B, OldCost_B, Flag, OldPrev),
            Flag = 0,
            New_Cost < OldCost_B,
            retract(city(B, OldCost_B, Flag, OldPrev)),
            assertz(city(B, New_Cost, 0, A))
        )
    ).


visited(A) :-
    retract(city(A, Dist, _, Prev)),
    assertz(city(A, Dist, 1, Prev)).