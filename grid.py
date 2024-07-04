# grid.py = Grid class

from typing import Optional

import textblock

#---------------------------------------------------------------------
"""
A 2-dimensional grid of colours
"""

GridCol = int # a colour of a square in a Grid
GridCols = list[int] # a list of Grid colours
OptGridCols = Optional[GridCols]


#---------------------------------------------------------------------
# colors

from colorist import Color, BrightColor, BgColor, BgBrightColor

SQUARE_TO_COLOR = [
    (0, BrightColor.WHITE, BgColor.BLACK),
    (1, BrightColor.WHITE, BgColor.BLUE),
    (2, BrightColor.WHITE, BgColor.RED),
    (3, BrightColor.WHITE, BgColor.GREEN),
    (4, Color.BLACK,       BgBrightColor.YELLOW),
    (5, BrightColor.WHITE, BgBrightColor.BLACK), # grey background
    (6, BrightColor.WHITE, BgColor.MAGENTA),
    (7, BrightColor.WHITE, BgBrightColor.RED), # orange, use bright red
    (8, Color.BLACK,       BgBrightColor.CYAN), # light blue
    (9, BrightColor.WHITE, BgColor.YELLOW), # brown background
]

SQ_FCOL = [fcol for c, fcol, bcol in SQUARE_TO_COLOR]
SQ_BCOL = [bcol for c, fcol, bcol in SQUARE_TO_COLOR]

#---------------------------------------------------------------------


class Grid:

    g: Optional[list[list[int]]] = None

    def __init__(self, initValue=None):
        if isinstance(initValue, list):
            self.g = makeCopy(initValue)
        elif isinstance(initValue, str):
            self.g = gFromStr(initValue)

    def copy(self) -> 'Grid':
        """ make as new Grid the same as this one """
        return Grid(self.lineStr())

    def at(self, r, c) -> GridCol:
        """ return the colour of the square at row r, col c.
        Returns -1 for off-grid
        """
        if self.g is None: return -1
        if r<0 or c<0: return -1
        if r>=len(self.g): return -1
        row = self.g[r]
        if c>=len(row): return -1
        return row[c]

    def rowColIndexes(self) -> list[tuple[int, int]]:
        """ return a list of all the row,column indexes.
        This should probasbly be a generator expression
        """
        if self.g is None: return []
        numRows = len(self.g)
        numCols = 0 if numRows==0 else len(self.g[0])
        result = []
        for r in range(numRows):
            for c in range(numCols):
                result.append((r,c))
        return result

    #===== output as text =====

    def __str__(self) -> str:
        """ output a representation of this grid """
        if not self.g: return "(empty)"
        result = ""
        for row in self.g:
            result += rowStr(row) + "\n"
        #//for
        return result[:-1]

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

    def ansiRow(self, r: int) -> str:
        """ output as a row in an ANSI-coloured str """
        line = self.g[r]
        result = ""
        for sq in line:
            result += SQ_FCOL[sq] + SQ_BCOL[sq]
            if sq==0:
                result += "."
            else:
                result += str(sq)
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
    """ Like `gridXYStr` in that it return a string showing the
    transformation from grid (x) to Grid (y). (text) is an annotation.
    However it insrets ANSI control codes into the output for colours.
    """


#---------------------------------------------------------------------

#end
