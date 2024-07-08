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






----
