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

----
