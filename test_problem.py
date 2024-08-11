# test_problem.py  = test <problem.py>



from utils.butil import *
from utils import lintest

import problem
from problem import Pair, Task

#---------------------------------------------------------------------
# data for tests

SAMPLE_PAIR = {
    "input":  [[1, 0, 0, 5, 0, 1, 0],
               [0, 1, 0, 5, 1, 1, 1],
               [1, 0, 0, 5, 0, 0, 0]],
    "output": [[0, 0, 0],
               [0, 2, 0],
               [0, 0, 0]]
}

SAMPLE_TASK = {
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

class T_Pair(lintest.TestCase):

    def test_creation(self):
        pr = Pair("create pair", SAMPLE_PAIR)
        self.assertSame(pr.x.at(0,3), 5, "value in input")
        self.assertSame(pr.y.at(1,1), 2, "value in output")
        self.assertSame(pr.y.at(1,2), 0, "value in output")
        self.assertSame(pr.desc, "create pair", "desc")
        prn(pr.ansi())


#---------------------------------------------------------------------

class T_Task(lintest.TestCase):

    def test_creation(self):
        t = Task("create task", SAMPLE_TASK)
        self.assertSame(len(t.train), 3, "number of training pairs")
        self.assertSame(len(t.test), 1, "number of tests")
        self.assertSame(t.name, "create task", "name")
        prn(t.ansi())

    def test_loadFromFile(self):
        t = Task()
        t.loadFromFile("data/arc_agi_training/007bbfb7.json")
        self.assertSame(len(t.train), 5, "number of training pairs")
        self.assertSame(len(t.test), 1, "number of tests")
        prn(t.ansi())

    def test_makeTask(self):
        t = problem.makeTask("turn right",
            train = [("1112/...2/..33", "..1/..1/3.1/322"),
                     ("54/00",".5/.4"),
                    ],
            test = [("..6../77677/..6../..6..","..7./..7./6666/..7./..7.")]
        )
        self.assertSame(len(t.train), 2, "# training pairs")
        self.assertSame(len(t.test), 1, "# test pairs")
        prn(t.ansi())

    def test_saveTask(self):
        """ save the sample task """

        #>>>>> remove json files
        self.cmd("rm -f testing/*.json")

        t = Task("create task", SAMPLE_TASK)
        t.saveToFile("testing/sample.json")
        self.assertFileExists("testing/sample.json")
        t2 = Task()
        t2.loadFromFile("testing/sample.json")
        self.assertBool(t2==t)

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_Pair)
group.add(T_Task)

if __name__=='__main__': group.run()

#end
