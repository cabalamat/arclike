# test_gridfun.py = test <gridfun.py>



from utils.butil import *
from utils import lintest

from grid import Grid, gridXYStr, gridXYAnsi
from gridfun import *

import textblock

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

    def test_nw(self):
        g = Grid("......../"
                 ".222222./"
                 ".2....2./"
                 ".2....2./"
                 ".222222./"
                 "........")
        g2 = setSquares(g, 8, nw=[2])
        sb =    ("......../"
                 ".222222./"
                 ".2888888/"
                 ".28...28/"
                 ".2822228/"
                 "..888888")
        r = g2.lineStr()
        self.assertSame(r, sb, "8 if nw=2")
        prn(f"g:\n{g}")
        prn(f"g2:\n{g2}")
        prn(gridXYStr("g->g2:", g, g2))
        prn(gridXYAnsi("g->g2:", g, g2))
        g3 = setSquares(g2, 6, e=[2], center=[0])
        prn(gridXYStr("g2->g3:", g2, g3))
        prn(gridXYAnsi("g2->g3:", g2, g3))

    def test_topRow(self):
        g = Grid("....../"
                 ".2222./"
                 ".2132./"
                 ".2452./"
                 ".6789./"
                 "......")
        g2 = setSquares(g, 3, n=[-1]) # -1 means off-board
        prn(gridXYAnsi("g->g2:", g, g2))
        sb =    ("333333/"
                 ".2222./"
                 ".2132./"
                 ".2452./"
                 ".6789./"
                 "......")
        r = g2.lineStr()
        self.assertSame(r, sb, "3 if n=-1")

    def test_edgesCorners(self):
        g = Grid("....../"
                 "....../"
                 ".1234./"
                 "....../"
                 "....../"
                 "......")
        g2 = setSquares(g, 7, n=[-1])
        g3 = setSquares(g2, 7, e=[-1])
        g4 = setSquares(g3, 7, s=[-1])
        g5 = setSquares(g4, 7, w=[-1])
        prn(gridXYAnsi("g->g5:", g, g5))
        sb =    ("777777/"
                 "7....7/"
                 "712347/"
                 "7....7/"
                 "7....7/"
                 "777777")
        r = g5.lineStr()
        self.assertSame(r, sb, "7 if n/s/e/w=-1")

        g6 = setSquares(g5, 6, n=[-1], w=[-1])
        g7 = setSquares(g6, 6, n=[-1], e=[-1])
        g8 = setSquares(g7, 6, s=[-1], w=[-1])
        g9 = setSquares(g8, 6, s=[-1], e=[-1])
        prn(gridXYAnsi("g5->g9:", g5, g9))
        sb =    ("677776/"
                 "7....7/"
                 "712347/"
                 "7....7/"
                 "7....7/"
                 "677776")
        r = g9.lineStr()
        self.assertSame(r, sb, "6 if at corner")

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_setSquares)

if __name__=='__main__': group.run()

