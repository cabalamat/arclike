# grid.py = Grid class

from typing import Optional


#---------------------------------------------------------------------
"""
A 2-dimensional grid of colours
"""

GridCol = int # a colour of a square in a Grid
GridCols = list[int] # a list of Grid colours
OptGridCols = Optional[GridCols]


#---------------------------------------------------------------------


class Grid:

    g: Optional[list[list[int]]] = None

    def __init__(self, initValue=None):
        if isinstance(initValue, list):
            self.g = makeCopy(initValue)
        elif isinstance(initValue, str):
            self.g = gFromStr(initValue)

    def __str__(self) -> str:
        """ output a representation of this grid """
        if not self.g: return "(empty)"
        result = ""
        for row in self.g:
            result += rowStr(row) + "\n"
        #//for
        return result[:-1]

    def lineStr(self) -> str:
        """ outpout as line-string """
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

    def prettyStr(self) -> str:
        """ output as pretty coloured str of this grid, including newlines """

    def prettyRow(self, r: int) -> str:

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

#end
