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
        self.assertSame(r, "222/222/222", "all squares now 2")

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_setSquares)

if __name__=='__main__': group.run()

