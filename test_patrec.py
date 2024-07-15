# test_patrec.py = test <patrec.py>


from utils.butil import *
from utils import lintest

from grid import Grid, gridXYStr, gridXYAnsi

from patrec import gridLoss # unit under test

#---------------------------------------------------------------------

class T_miscFuns(lintest.TestCase):
    """ test miscellaneous functions """

    def test_gridLoss_same(self):
        """ test gridLoss when given the same grid """
        g1 = Grid("66/77")
        gt = Grid("66/77")
        r = gridLoss(g1, gt)
        prn(gridXYAnsi("gridLoss sb 0", g1, gt))
        self.assertSame(r, 0, "both grids same")

        g1 = Grid(".33./3..3/.44./2..2/.22.")
        gt = Grid(".33./3..3/.44./2..2/.22.")
        r = gridLoss(g1, gt)
        prn(gridXYAnsi("gridLoss sb 0", g1, gt))
        self.assertSame(r, 0, "both grids same")

    def test_gridLoss_targetBigger(self):
        """ the target is bigger, should look at squares that exist in target,
        penalize g1 for all square's its missing,
        then add 1 for different size. """
        g1 = Grid("66/77")
        gt = Grid("66./77./...")
        r = gridLoss(g1, gt)
        prn(gridXYAnsi("gridLoss sb 6", g1, gt))
        self.assertSame(r, 6, "5 sq missing + different extent")

    def test_gridLoss_gBigger(self):
        """ the (g) arg is bigger, should look at squares that exist in target,
        check on squares in g that're within target's extent,
        then add 1 for different size. """
        g1 = Grid("66./77./...")
        gt = Grid("66/77")
        r = gridLoss(g1, gt)
        prn(gridXYAnsi("gridLoss sb 1", g1, gt))
        self.assertSame(r, 1, "different extent")


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_miscFuns)

if __name__=='__main__': group.run()


#end
