# test_textblock.py = test <textblock.py>


from utils.butil import *
from utils import lintest

from textblock import * # module under test

#---------------------------------------------------------------------

class T_getExtent(lintest.TestCase):
    """ test getExtent() """

    def test_empty(self):
        r,c = getExtent("")
        self.assertSame((r,c), (0,0), "empty string")

    def test_1(self):
        r,c = getExtent("this\nis\na\ngood\nstring")
        self.assertSame((r,c), (5,6))

    def test_empty_lines(self):
        r,c = getExtent("this\n\n\n\nstring")
        self.assertSame((r,c), (5,6))


#---------------------------------------------------------------------

class T_makeSize(lintest.TestCase):
    """ test makeSize() """

    def test_1(self):
        r = makeSize("hello", 3, 6)
        sb = "hello \n      \n      "
        self.assertSame(r, sb, "padded to 3 rows, 6 columns")


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_getExtent)
group.add(T_makeSize)
#group.add(T_getRow)
#group.add(T_joinTextRects)

if __name__=='__main__': group.run()

#end
