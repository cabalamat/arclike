# driver.py = calls <grid.py>


from utils.butil import prn

import grid
from grid import Grid


#---------------------------------------------------------------------


def driveGrid():
    prn("===== driveGrid() =====")
    g1 = Grid("..../.1../....")
    prn(f"g1=\n{g1}")



if __name__=='__main__':
    driveGrid()

#end
