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
        dpr("solv.funRack=%s", solv.funRack)
        dpr("solv.funRack:")
        for ix, fun in kv(solv.funRack):
            prn("[%s] %s", ix, fun)

    def test_1ply(self):
        """ create a solver, then expand nodes 1 ply with all the GridFuns
        in the funRack.
        """
        #>>>>> first make a Task
        t = problem.makeTask("turn right",
            train = [("1112/...2/..33", "..1/..1/3.1/322"),
                     ("54/00",".5/.4"),
                    ],
            test = [("..6../77677/..6../..6..","..7./..7./6666/..7./..7.")]
        )
        self.assertSame(len(t.train), 2, "# training pairs")
        self.assertSame(len(t.test), 1, "# test pairs")
        prn(t.ansi())

        #>>>>> then put it in a Solver
        solv = Solver(t)
        dpr("solv.funRack:")
        for ix, fun in kv(solv.funRack):
            prn("[%s] %s", ix, fun)
        numFuns = len(solv.funRack)
        self.assertTrue(numFuns >= 2, "at least 2 funs in funRack")

        #>>>>> expand one level
        solv.expand()

        solv


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_Solver)
#group.add(T_Node)

if __name__=='__main__': group.run()

#end
