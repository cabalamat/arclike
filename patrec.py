# patrec.py = pattern recognisers

from abc import ABC, abstractmethod # abstract base classes

import grid
from grid import Grid
import gridfun
import problem
from problem import Task

#---------------------------------------------------------------------
# abstract class for pattern recognisers

class PatRec(ABC):

    def searchOnTask(self, t: Task):
        """ search for functions thta telk to solve (t) """
        self.searchOnGrids(t.x, t.y)

    @abstractmethod
    def searchOnGrids(self, gx: Grid, gy: Grid):
        """ search for functions that when applied to (gx) make
        it more similar to (gy).
        """


#---------------------------------------------------------------------

class ChangeColorRec(PatRec):
    """ a PatRec that looks for functiomns that change all squares that're
    one colour to another colour.
    """
    gx: Grid
    gy: Grid
    colChange: list[list[int]]


    def searchOnGrids(self, gx: Grid, gy: Grid):
        """ search for functions that when applied to (gx) make
        it more similar to (gy).
        """
        self.gx = gx
        self.gy = gy
        self.colChangeTable()


    def colChangeTable(self):
        """ calc a colour change table, i.e. one that looks in every square
        in (gx) and its correspondance to the same square in (gy).
        """
        self.colChange = makeColTable()
        for r, c in gx.rowColIndexes():
            gxSq = gx.at(r, c)
            gySq = gy.at(r, c)
            if gySq == grid.COL_OFFBOARD:
                continue
            self.colChange[gxSq][gySq] += 1
        #//for r, c
        prn("self.colChange=\n{}", self.colChange)




#---------------------------------------------------------------------

def gridLoss(g: Grid, target: Grid) -> int:
    """ measures how dissimilar (g) is to what it's meant to be, i.e.
    the (target).
    0 = the same
    higher numbers mean less similar.
    """
    loss = 0
    for tr, tc in target.rowColIndexes():
        if g.at(tr, tc) != target.at(tr, tc):
            loss += 1
    #//for tc, tr
    if g.extent() != target.extent():
        loss += 1
    return loss

def makeColTable() -> list[list[int]:
    """ return a colour change table, initialised to zeroes """
    size = grid.COL_MAX + 1
    result = []
    for x in range(size):
        for y in range(size):
            row = [0]*size
        #//for y
        result += [row]
    #//for x
    return result



#end
