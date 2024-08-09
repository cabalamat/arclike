# gridfun.py = functions on Grids

from grid import Grid, GridCol, GridCols, OptGridCols

#---------------------------------------------------------------------

class GridFun:
    """ a GridFun is a function that acts on a grid producing another
    grid. Note that all functions are deterministic and withoutr internal
    states.
    """

    def run(self, g: Grid) -> Grid:
        """ run the function """

    def isIdempotent(self) -> bool:
        """ an idempotent function is one where if you do it multiple times,
        only the first time has an effect, i.e. f(f(g))==f(g).
        The purpose of knowing this is to reduce the size of the search
        tree, by not applying the same function twice.
        """
        return False

    def isOwnInverse(self) -> bool:
        """ A function is its own inverse if for all inputs f(f(g))==g.
        The purpose of knowing this is to reduce the size of the search
        tree, by not applying the same function twice.
        """
        return False

    def __str__(self):
        """ print a representation of me """
        return self.__class__.__name__


#---------------------------------------------------------------------

def setSquares(g: Grid,
               newValue: GridCol,
               nw: OptGridCols =None,
               n: OptGridCols =None,
               ne: OptGridCols =None,
               w: OptGridCols =None,
               center: OptGridCols =None,
               e: OptGridCols =None,
               sw: OptGridCols =None,
               s: OptGridCols =None,
               se: OptGridCols =None
    ) -> Grid:
    """ output a new grid the same dimesions as (g).
    The new grid will be a copy of the old grid, except where a pattern matches,
    when the center square will be replaced by (newValue).
    """
    criteria = {}
    if nw: criteria['nw'] = nw
    if n:  criteria['n'] = n
    if ne: criteria['ne'] = ne
    if w:  criteria['w'] = w
    if center: criteria['center'] = center
    if e:  criteria['e'] = e
    if sw: criteria['sw'] = sw
    if s:  criteria['s'] = s
    if se: criteria['se'] = se

    newGrid = g.copy()
    for r, c in g.rowColIndexes():
        if criteriaMatch(g, r, c, criteria):
            newGrid.g[r][c] = newValue
    #//for r,c
    return newGrid

# for each direction, include name, row offset, column offset
DIRECTIONS = [
    ('nw',     -1, -1),
    ('n',      -1,  0),
    ('ne',     -1,  1),
    ('w',       0, -1),
    ('center',  0,  0),
    ('e',       0,  1),
    ('sw',      1, -1),
    ('s',       1,  0),
    ('se',      1,  1),
]


def criteriaMatch(g: Grid, r: int, c: int, criteria: dict) -> bool:
    """ do the criteria match at location [r][c] of Grid g? """
    for dirName, rOff, cOff in DIRECTIONS:
        if dirName not in criteria: continue

        rIx = r + rOff
        cIx = c + cOff
        valueAt = g.at(rIx, cIx)
        if valueAt not in criteria[dirName]:
            # value must be one of the ones specified in the criteria
            return False
    #//for
    return True


#---------------------------------------------------------------------
# rotation functions

def rotc(g: Grid) -> Grid:
    """ rotate clockwise """
    yg = list(zip(*g.g[::-1]))
    return Grid(yg)

def rotc2(g: Grid) -> Grid:
    """ rotate through 180 degrees (i.e. clockwise twice) """
    yg = [r[::-1] for r in g.g[::-1]]
    return Grid(yg)

def rotc3(g: Grid) -> Grid:
    """ rotate anti-clockwise (i.e. clockwise three times) """
    return rotc(rotc2(g))

class Rotc(GridFun):
    def run(self, g: Grid) -> Grid:
        return rotc(g)

class Rotc2(GridFun):
    def run(self, g: Grid) -> Grid:
        return rotc2(g)

    def isOwnInverse(self) -> bool:
        return True

class Rotc3(GridFun):
    def run(self, g: Grid) -> Grid:
        return rotc3(g)


#---------------------------------------------------------------------
"""
From <https://www.kaggle.com/code/michaelhodel/program-synthesis-starter-notebook/notebook>
This removes rows and columns that're all the same colour.
"""

def compress_ll(grid: list[list[int]]) -> list[list[int]]:
    """ removes rows and columns that're all the same colour """
    ri = [i for i, r in enumerate(grid) if len(set(r)) == 1]
    ci = [j for j, c in enumerate(zip(*grid)) if len(set(c)) == 1]
    result = [[v for j, v in enumerate(r) if j not in ci]
              for i, r in enumerate(grid) if i not in ri]
    return result

def compress(g: Grid) -> Grid:
    newGg = compress_ll(g.g)
    return Grid(newGg)

class Compress(GridFun):
    def run(self, g: Grid) -> Grid:
        return compress(g)


#---------------------------------------------------------------------

def initialFunRack() -> list[GridFun]:
    """ return the initial funrack to be used by Solvers """
    ifr = [
        Rotc(),
        Rotc2(),
        Rotc3(),
        Compress(),
    ]
    return ifr

#---------------------------------------------------------------------

#end
