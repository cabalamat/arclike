# test_patrec.py = test <patrec.py>


from utils.butil import *
from utils import lintest

from grid import Grid, gridXYStr, gridXYAnsi

from patrec import gridLoss # unit under test

#---------------------------------------------------------------------

class T_gridLoss(lintest.TestCase):
    """ test the groidLoss function """

    def testGridLoss(self, g1, g2, sb):
        r = gridLoss(g1, g2)
        prn(gridXYAnsi(f"gridLoss sb {sb} is {r}", g1, g2))
        self.assertSame(r, sb, "testing gridLoss()")
        r2 = gridLoss(g2, g1)
        self.assertSame(r2, r, "same gridLoss() when arguments reversed")

    def test_gridLoss_same(self):
        """ test gridLoss when given the same grid """
        g1 = Grid("66/77")
        gt = Grid("66/77")
        self.testGridLoss(g1, gt, 0)

        g1 = Grid(".33./3..3/.44./2..2/.22.")
        gt = Grid(".33./3..3/.44./2..2/.22.")
        self.testGridLoss(g1, gt, 0)

    def test_gridLoss_targetBigger(self):
        """ the target is bigger """
        g1 = Grid("66/77")
        gt = Grid("66./77./...")
        self.testGridLoss(g1, gt, 2)

    def test_gridLoss_same(self):
        """ test gridLoss when given the same grid """
        g1 = Grid(".123./.456./.789.")
        gt = Grid(".444./.555./.666.")
        self.testGridLoss(g1, gt, 8)




#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_gridLoss)

if __name__=='__main__': group.run()


#end
