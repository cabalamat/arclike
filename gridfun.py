# gridfun.py = functions on Grids

from grid import Grid, GridCol, GridCols, OptGridCols

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


#---------------------------------------------------------------------

#---------------------------------------------------------------------

#end
