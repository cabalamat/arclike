# grid.py = Grid class

from typing import Optional
from utils.butil import form, printargs, dpr

import textblock

#---------------------------------------------------------------------
"""
A 2-dimensional grid of colours

Colour values in squares are 0..9.
-1 = off-board
-2 = transparent (for computed grids used intermediate results)
"""

GridCol = int # a colour of a square in a Grid
GridCols = list[int] # a list of Grid colours
OptGridCols = Optional[GridCols]
COL_OFFBOARD = -1
COL_TRANSPARENT = -2
COL_MAX = 9 # colours go from 0 to COL_MAX


#---------------------------------------------------------------------
# ansi colours for console display

from colorist import Color, BrightColor, BgColor, BgBrightColor

SQUARE_TO_COLOR = [
    (0, BrightColor.WHITE, BgColor.BLACK),
    (1, BrightColor.WHITE, BgColor.BLUE),
    (2, BrightColor.WHITE, BgColor.RED),
    (3, BrightColor.WHITE, BgColor.GREEN),
    (4, Color.BLACK,       BgBrightColor.YELLOW),
    (5, BrightColor.WHITE, BgBrightColor.BLACK), # grey background
    (6, BrightColor.WHITE, BgColor.MAGENTA),
    (7, Color.BLACK,       BgBrightColor.RED), # orange, use bright red
    (8, Color.BLACK,       BgBrightColor.CYAN), # light blue
    (9, BrightColor.WHITE, BgColor.YELLOW), # brown background
]

SQ_FCOL = [fcol for c, fcol, bcol in SQUARE_TO_COLOR]
SQ_BCOL = [bcol for c, fcol, bcol in SQUARE_TO_COLOR]

#---------------------------------------------------------------------


class Grid:
    g: list[list[int]] = []

    def __init__(self, initValue=None):
        if isinstance(initValue, list):
            self.g = initValue
        elif isinstance(initValue, str):
            self.g = gFromStr(initValue)

    def copy(self) -> 'Grid':
        """ make as new Grid the same as this one """
        return Grid(self.lineStr())

    def at(self, r, c) -> GridCol:
        """ return the colour of the square at row r, col c.
        Returns -1 for off-grid
        """
        if self.isOffBoard(r, c): return COL_OFFBOARD
        #dpr("self={} r={} c={}", self.lineStr(), r, c)
        return self.g[r][c]

    def rowColIndexes(self) -> list[tuple[int, int]]:
        """ return a list of all the row,column indexes.
        This should probably be a generator expression
        """
        if self.g is None: return []
        numRows = len(self.g)
        numCols = 0 if numRows==0 else len(self.g[0])
        result = []
        for r in range(numRows):
            for c in range(numCols):
                result.append((r,c))
        return result

    def rowIndexes(self) -> list[int]:
        """ return a list of all the row indexes.
        This should probably be a generator expression
        """
        return list(range(len(self.g)))

    def extent(self) -> tuple[int, int]:
        """ return size as (numRows, numCols) """
        nr = self.numRows()
        if nr==0:
            nc = 0
        else:
            nc = len(self.g[0])
        return nr, nc

    def isOffBoard(self, r: int, c: int) -> bool:
        """ is location (r,c) off board? """
        if r<0 or c<0: return True
        nr, nc = self.extent()
        #dpr("self={} r={} c={} nr={} nc={}", self.lineStr(), r, c, nr, nc)
        if r>=nr or c>=nc: return True
        return False


    def numRows(self) -> int:
        return len(self.g)


    #===== output as text =====

    def __str__(self) -> str:
        """ output a representation of this grid """
        if not self.g: return "(empty)"
        result = ""
        for row in self.g:
            result += rowStr(row) + "\n"
        #//for
        return result

    def lineStr(self) -> str:
        """ output as line-string """
        result = ""
        for row in self.g:
            for sq in row:
                if sq==0:
                    result += "."
                else:
                    result += str(sq)
            #//for sq
            result += "/"
        #//for row
        return result[:-1]

    #===== output coloured using ANSI codes =====

    def ansiStr(self) -> str:
        """ output as an ANSI-coloured str of this grid, including newlines """
        result = ""
        for r in self.rowIndexes():
            result += self.ansiRow(r) + "\n"
        return result

    def ansiRow(self, r: int) -> str:
        """ output as a row in an ANSI-coloured str """
        xr, xc = self.extent()
        if r<0 or r>=xr:
            return "  "*xc
        line = self.g[r]
        result = ""
        for sq in line:
            result += SQ_FCOL[sq] + SQ_BCOL[sq]
            if sq==0:
                result += " ."
            else:
                result += " " + str(sq)
        result += Color.DEFAULT + BgColor.DEFAULT
        return result


#---------------------------------------------------------------------
# helper functions for grids

def rowStr(row: list[int]) -> str:
    """ get a string from a row """
    result = ""
    for sq in row:
        if sq==0:
            result += "."
        else:
            result += str(sq)
    return result


def gFromStr(s: str) -> list[list[int]]:
    """ create the internals of a grid from a line-string,
    e.g. "12/34" -> [[1,2], [3,4]]

    digits go to that digit, "/" means new row
    "." means 0, anything else is undefined.
    """
    result = []
    row = []
    for ch in s:
        if ch==".": ch = "0"
        if ch in "0123456789":
            d = int(ch)
            row.append(d)
        elif ch=="/":
            result.append(row)
            row = []
    #//for
    if row:
        result.append(row)
    return result

#---------------------------------------------------------------------


def gridXYStr(text:str, x: Grid, y: Grid) -> str:
    """ Return a string showing the transformation from grid (x) to
    Grid (y). (text) is an annotation.
    """
    return textblock.joinTextRects(text, str(x), "->", str(y))

def gridXYAnsi(text:str, x: Grid, y: Grid) -> str:
    """ Like `gridXYStr()` in that it returns a string showing the
    transformation from grid (x) to Grid (y). (text) is an annotation.
    However it insrets ANSI control codes into the output for colours.
    """
    numRows = 0
    textRows, textCols = textblock.getExtent(text)
    numRows = max(numRows, textRows)
    for g in [x,y]:
        numRows = max(numRows, g.numRows())
    #//for g

    textArr = textblock.makeRightSize(text, numRows)
    arrowArr = textblock.makeRightSize("->", numRows)

    result = ""
    for r in range(numRows):
        result += form("{} {} {} {}\n",
            textArr[r],
            x.ansiRow(r),
            arrowArr[r],
            y.ansiRow(r))
    #//for r
    return result



#---------------------------------------------------------------------



#end
