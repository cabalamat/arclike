# test_gridfun.py = test <gridfun.py>



from utils.butil import *
from utils import lintest

from grid import Grid
from gridfun import *

#---------------------------------------------------------------------

class T_setSquares(lintest.TestCase):
    """ test setSquares() """

    def test_center_unconditional(self):
        """ change the square at the center """
        g = Grid("111/111/111")
        g2 = setSquares(g, 2) # set all squares to 2
        r = g2.lineStr()
        self.assertSame(r, "222/222/222", "all squares 1->2")

        g3 = Grid("1234/5009")
        g4 = setSquares(g3, 8) # set all squares to 8
        r = g4.lineStr()
        self.assertSame(r, "8888/8888", "all squares ?->8")

    def test_center_conditional(self):
        """ change the square at the center """
        g = Grid("01234/56789")
        g2 = setSquares(g, 2, center=[3,6]) # set all squares to 2 if 3 or 6
        r = g2.lineStr()
        self.assertSame(r, ".1224/52789", "all squares 3,6->2")

    def test_n(self):
        g = Grid("...../34567/.....")
        g2 = setSquares(g, 8, n=[3,7])
        r = g2.lineStr()
        self.assertSame(r, "...../34567/8...8", "if n is 3,7->8")

        g = Grid("...../34567/11111")
        g2 = setSquares(g, 8, n=[3,7])
        r = g2.lineStr()
        self.assertSame(r, "...../34567/81118", "if n is 3,7->8")

    def test_n_center(self):
        g = Grid("...../34567/.....")
        g2 = setSquares(g, 8, n=[3,7], center=[0])
        r = g2.lineStr()
        self.assertSame(r, "...../34567/8...8",
            "if n is 3,7 and center 0 ->8")

        g = Grid("...../34567/111..")
        g2 = setSquares(g, 8, center=[0], n=[3,7])
        r = g2.lineStr()
        self.assertSame(r, "...../34567/111.8",
            "if n is 3,7 and center 0 ->8")


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_setSquares)

if __name__=='__main__': group.run()

