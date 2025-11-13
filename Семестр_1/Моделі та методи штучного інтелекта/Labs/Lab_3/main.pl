:- dynamic city/4.


node(a,b,50).
node(b,a,50).

node(a,c,80).
node(c,a,80).

node(b,c,30).
node(c,b,30).

node(c,d,100).
node(d,c,100).

node(b,d,50).
node(d,b,50).


newcity:-
    retractall(city(_,_,_,_)),
    forall(node(X,Y,_),
    (
        ((\+ (city(X,_,_,_))) -> assert(city(X,1000000000,0,none)) ; true),

        ((\+ (city(Y,_,_,_))) -> assert(city(Y,1000000000,0,none)) ; true)
    )).


findway(A,B,Size,Last):-

    newcity,
    retract(city(A,_,_,_)),
    assert(city(A,0,0,none)),
    
    deskre, 

    city(B,Size,_,_),

    path(B,Last).

path(B,Path):-
    path(B,[],Path).

path(none, MustReturnResult, MustReturnResult):-!.

path(Element,LastPath,NewPath):-
    city(Element,_,_,LastElement),
    path(LastElement,[Element|LastPath],NewPath).


deskre:-
    setof(Cost-Name, city(Name,Cost,0,_), Result),
    (
        Result=[] -> true ; (
        
        Result = [_-NameBest|_],

        cost(NameBest),
        visited(NameBest),
        deskre
        )

    ).

deskre:-true.

cost(A):-
    city(A,OldCost,_,_),
    forall(node(A,B,TempCost),
        (
        
            NewCost is TempCost + OldCost,

            
            city(B,Cost,0,_),
            
            NewCost < Cost ->(
                retract(city(B,_,C,_)),
                assert(city(B,NewCost,C,A))
            );true
        )
    
    ).

visited(A):-
    retract(city(A,B,_,D)),
    assert(city(A,B,1,D)).
