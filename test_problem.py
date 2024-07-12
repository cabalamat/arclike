# test_problem.py  = test <problem.py>



from utils.butil import *
from utils import lintest

from problem import Task, Problem

#---------------------------------------------------------------------
# data for tests

SAMPLE_TASK = {
    "input":  [[1, 0, 0, 5, 0, 1, 0],
               [0, 1, 0, 5, 1, 1, 1],
               [1, 0, 0, 5, 0, 0, 0]],
    "output": [[0, 0, 0],
               [0, 2, 0],
               [0, 0, 0]]
}

SAMPLE_PROBLEM = {
 "train": [
    {"input":  [[1, 0, 0, 5, 0, 1, 0],
                [0, 1, 0, 5, 1, 1, 1],
                [1, 0, 0, 5, 0, 0, 0]],
     "output": [[0, 0, 0],
                [0, 2, 0],
                [0, 0, 0]]},
    {"input":  [[1, 1, 0, 5, 0, 1, 0],
                [0, 0, 1, 5, 1, 1, 1],
                [1, 1, 0, 5, 0, 1, 0]],
     "output": [[0, 2, 0],
                [0, 0, 2],
                [0, 2, 0]]},
    {"input":  [[0, 0, 1, 5, 0, 0, 0],
                [1, 1, 0, 5, 1, 0, 1],
                [0, 1, 1, 5, 1, 0, 1]],
     "output": [[0, 0, 0],
                [2, 0, 0],
                [0, 0, 2]]}],
 "test": [
    {"input":  [[1, 0, 1, 5, 1, 0, 1],
                [0, 1, 0, 5, 1, 0, 1],
                [1, 0, 1, 5, 0, 1, 0]],
     "output": [[2, 0, 2],
                [0, 0, 0],
                [0, 0, 0]]}]
}


#---------------------------------------------------------------------

class T_Task(lintest.TestCase):

    def test_creation(self):
        tk = Task("create_task", SAMPLE_TASK)
        self.assertSame(tk.x.at(0,3), 5, "value in input")
        self.assertSame(tk.y.at(1,1), 2, "value in output")
        self.assertSame(tk.y.at(1,2), 0, "value in output")
        self.assertSame(tk.desc, "create_task", "desc")
        prn(tk.ansi())


#---------------------------------------------------------------------

class T_Problem(lintest.TestCase):

    def test_creation(self):
        prob = Problem("create_problem", SAMPLE_PROBLEM)
        self.assertSame(len(prob.train), 3, "number of training tasks")
        self.assertSame(len(prob.test), 1, "number of tests")
        self.assertSame(prob.name, "create_problem", "name")
        prn(prob.ansi())

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_Task)
group.add(T_Problem)

if __name__=='__main__': group.run()


#end

#end
