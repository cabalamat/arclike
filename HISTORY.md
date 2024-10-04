# HISTORY.md for arclike

New stuff goes at bottom. Use "##" for headings, dates go in format 2021-Dec-31.

----

## 2024-Jun-16: created

## 2024-Jul-02: put in git

## 2024-Jul-02

Added wiki (in wiki/).

Working on displaying grids on console like this:

```
..... -> .8...
12345    12345
.....    ...8.
```

Where "." == 0 == black.

Done as `grid.gridXYStr()`.

## 2024-Jul-04

Do same as `gridXYStr()` but with colours. Using the `colorist` package for this.

-- got colorist basic functionaslity working in `Grid.ansiRow()`

grid.gridXYAnsi() draws 2 coloured grid (x,y) using ansi terminal colours. Working

## 2024-Jul-07

`setSquares()` doesn't work for off-board.

`setSquares(g, 3, n=[-1])` should colour the top row colour 3 but it's not working.
See testgridfun >> T_setSquares.test_topRow -- FIXED

## 2024-Jul-08

TODO: write `Problem` class. A Problem is a set of 2 grids, representing the
input to and output from a function. -- DONE


## 2024-Jul-14

Started working on <patrec.py> which will contain pattern recognisers.
The first patrec will be a very simple one that changes all squares that're one colour to another.

## 2024-Jul-27

Rewriting patrec.gridLoss function. It should give the same answer when the
parameters are switched round.

```
    gridLoss = (number of squares different in the 2 grids)
               + deltaHeight + deltaWidth
```

where we look at the (r,c) coords common to both grids and deltas are the
difference in heights/widths between the 2 grids.

In grid, write extentIterator().

## 2024-Jul-31

My next goals...

Goal (1): in <problem.py> get `Problem` to be able to download problems from
various repositories of problems and prettyprint them.

Also create some of my own (simple) problems.

Goal (2): in <funrack.py> do a search of any two of my parameterless GridFuns
over a problem and see what the loss function is for all of them.

## 2024-Aug-07

My terminology is different from ARC-AGI's. Change from my old terminology
to ARC-AGI's, so:

Task -> Pair
Problem -> Task

## 2024-Aug-08

Change <funrack.py> to <solver.py>.

## 2024-Aug-10

Solver now expands 1 ply.

TODO:

Tidy up solver code

Add ability to write tasks to disk. Write tasks that exercise all the
parameterless GridFuns; put them in a directory <very_easy/>.
Write some more parameterless GridFuns.

Write a **runner** which attempts to solve all the very_easy tasks.

## 2024-Aug-11

Can now save tasks to disk.

## 2024-Aug-19

Started <runner.py> which pulls it all together and trys to solve a series
of problems stored on disk.

TODO:

Fix bug where solver nodes have loss incorrectly at 0.

In `Node.expand()`, made the function take a parameter depth (which defaults
to 1) meaning the depth to expand to.

The helper function `Node.expandWith()` should check that the expansion
node we're trying to create doesn't already exist.

## 2024-Oct-04

Creating new module <node.py> to preplace <solver.py> (which incidently is
badly named as the actually solving code will mostly go in <runner.py>.

The reason for this is to separate responsibilities: <node.py> will
know abnout nodes connecting to other nodes. It won't know about
the `funRack` as that's the responsibility ot the solving code.



----
