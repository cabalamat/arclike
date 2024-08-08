# test_solver.py = test <solver.py>


from utils.butil import *
from utils import lintest

import problem
from problem import Task

import solver # unit under test
from solver import Node, Solver

#---------------------------------------------------------------------

class T_Solver(lintest.TestCase):

    def setUpAll(self):
        """ this is run once before all tests """
        self.tk = Task()
        self.tk.loadFromFile("data/arc_agi_training/178fcbfb.json")
        prn(self.tk.ansi())


    def test_creation(self):
        solv = Solver(self.tk)

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_Solver)
#group.add(T_Node)

if __name__=='__main__': group.run()

#end
