# test_grid.py = test <grid.py>



from utils.butil import *
from utils import lintest

from grid import Grid, gridXYAnsi

#---------------------------------------------------------------------

class T_Grid(lintest.TestCase):
    """ test grids """

    def test_creation(self):
        g = Grid("123/456/..9")
        self.assertSame(g.g, [[1,2,3], [4,5,6], [0,0,9]],
            "create grid from line-string")

    def test_lineStr(self):
        """ the lineStr() method """
        g = Grid(".3./456/.3.")
        r = g.lineStr()
        self.assertSame(r, ".3./456/.3.")

        g = Grid("00000/44411/00000")
        r = g.lineStr()
        self.assertSame(r, "...../44411/.....")

    def test_copy(self):
        g = Grid(".123/4567/89..")
        g2 = g.copy()
        self.assertSame(g2.lineStr(), ".123/4567/89..", "g2 the same as g")

        g2.g[1][2] = 2
        self.assertSame(g2.lineStr(), ".123/4527/89..", "g2 row1 col2 = 2")
        self.assertSame(g.lineStr(), ".123/4567/89..",
            "g row1 col2 = 6 (unchanged)")

    def test_at(self):
        g = Grid("9999/8888/7654")
        r = g.at(0,0)
        self.assertSame(r, 9, "0,0 is 9")
        r = g.at(1,1)
        self.assertSame(r, 8, "1,1 is 8")
        r = g.at(2,0)
        self.assertSame(r, 7, "2,0 is 7")
        r = g.at(2,3)
        self.assertSame(r, 4, "2,3 is 4")
        r = g.at(-1,0)
        self.assertSame(r, -1, "-1,0 is off-grid")
        r = g.at(2,-7)
        self.assertSame(r, -1, "2,-7 is off-grid")
        r = g.at(3,0)
        self.assertSame(r, -1, "3,0 is off-grid")
        r = g.at(0,4)
        self.assertSame(r, -1, "0,4 is off-grid")

    def test_printing(self):
        g = Grid("....11...99/"
                 ".222..33399/"
                 ".2.2..44.9./"
                 ".2221.5559./"
                 ".1.11166.9./"
                 ".1.11.66.9./"
                 ".123456789./"
                 ".1.1..66.9./"
                 "9999..7779./"
                 "9..9..88.9./"
                 "99.9999999.")
        prn(f"Grid g:\n{g}")
        prn("ansi Grid g:\n{}", g.ansiStr())

        g2 = Grid("222..3/"
                  "2.2..4/"
                  "2221.5/"
                  ".1.111")
        prn("gridXYAnsi:\n{}", gridXYAnsi("g->g2", g, g2))


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_Grid)

if __name__=='__main__': group.run()


#end

