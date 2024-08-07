# Notes on Arclike architecture

Some notes on the architecture of my [[Arclike]] program.

[TOC]

## First version

The program will have an array of GridFuns. A GridFun transforms a Grid to another Grid.

Using notation that's a mixture between Python and Haskell we could say:

    GridFun :: Grid -> Grid

A sequence of GridFuns is invoked on the in put of a training pair, until it produces the desired output (i.e. the loss function is 0).

## Second version

Here a GridFun can take different types of input, and produce different types of output.

E.g. a GridFun might take a Grid and return the most-used Colour in it. Its type signature would thus be:

    Grid -> Colour

Or if it returns all the colours in order of the most used, it might be:

    Grid -> list[Colour]

Or it might split up a Grid into a number of smaller Grids:

    Grid -> list[Grid]

If your output is `list[Grid]` but you want a `Grid`, then you might look for a converter program with the type signature `list[Grid]->Grid`.
This might take the zeroth index, and if the list is empty it might instead return a null Grid.

Think if it as adding circuits together, with different types of signals, where the shape of the plugs and sockets mean you can only join together correct types.

### Type signatures

Primitive types might include `Grid`, `Colour`, `int`

Collection types might include `list`, `set`.

## Third version

Like the second version except that every output is labelled (i.e. assigned to an identifier) and the later stages of the chain can refer to named results and not just the most recent one.

Also have loops: continue applying a function until the output no longer changes. E.g. if your function is "any square that is 0 and has 3 to the west of it, make 3", then continually applying it would convert:

```
..3....   ->  ..33333
.....3.       .....33
2.3.6..       2.336..
...35..       ...35..
```

There would be macro-function: a load of functions wrapped together to make another function.

## Fourth version

As above, except that our functions should also be able to return functions as outputs. E.g. we could have a function
that takes 2 grids as input , and returns another function that transforms its input (a Grid) into something hopefully like the 2nd Grid of input.
Its type signature would be something like (in our notation):

    (Grid, Grid) -> (Grid -> Grid)

In Python notation this might be:

```py
def myFun(x: Grid, y: Grid) -> Callable[[Grid], Grid]
    """ (x) and (y) are the input and output parts of a training pair respectively.
    The output is a transformation function, that transforms a Grid (gx)
    into another Grid (gy).
    """

```

But in Haskell its type signature would be the simpler:

```hs
myFun :: Grid -> Grid -> Grid -> Grid
```

Which uses partial application.

Hey, maybe we should invent our our programming language for writing GridFuns! (only serious)

## Varients

* have simpler I/O types, e.g. instead of a grid, a string.
* have more complex I/O types, e.g. instead of a Grid and arbitrary JSON value.

## Training a NN

NB in ARC-AGI the tasks are to some extent (but not as much as in Copycat) [[patterns not functions]].


