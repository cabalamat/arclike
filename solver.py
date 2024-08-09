# solver.py = attempts to solve a Task

"""
Solver attempts to solve a task.
"""

from typing import Union, Optional, Any

from utils import butil
from utils.butil import prn, dpr, form

from grid import Grid
from problem import Task, Pair
import gridfun
from gridfun import GridFun

#---------------------------------------------------------------------
"""
A Node is the result of applying a GridFun to as series of training pair
inputs
"""

class Node:
    parent: 'Node'
    fun: GridFun
    loss: int = 0
    children: list['Node'] = [] # nodes expanded from here

    # tpy = Training-Pair Y (y=output)
    tpy: list[Grid] = []

    def getSolver(self) -> 'Solver':
        """ go up through my ancestors until we reach the solver """
        return self.parent.getSolver()

    def getTargetOutputs(self) ->  list[Grid]:
        return self.getSolver().targetOutputs

    def getFunRack(self) -> list[GridFun]:
        return self.getSolver().funRack

    def expand(self):
        self.children = [self.expandWith(gf)
                         for gf in self.getFunRack()]

    def expandWith(self, gf: GridFun) -> 'Node':
        """ expand myself using (gf) to create a new Node.
        Return that node.
        """
        newNode = Node()
        newNode.parent = self
        newNode.fun = gf
        newNode.calcTpyEtc()
        return newNode

    def calcTpyEtc(self):
        """ For this newly-created node, calculate:
        (self.tpy) = outout from applying (self.fun)
        (self.loss) = loss compasring (self.tpy) with targetOutputs
        """
        dpr("{} enters calcTpyEtc()", self)


    def __str__(self):
        s = self.parent.__str__()
        s += "|"
        s += self.fun.__str__()
        return s



#---------------------------------------------------------------------
"""
A Solver is the head-node to a Task
"""

class Solver(Node):
    task: Task
    numTrainingPairs: int
    targetOutputs: list[Grid]
    funRack: list[GridFun]

    #===== initialisation

    def __init__(self, tk: Task):
        self.task = tk
        self.numTrainingPairs = len(self.task.train)
        assert self.numTrainingPairs > 0
        self.tpy = [pair.x for pair in tk.train]
        self.targetOutputs = [pair.y for pair in tk.train]
        self.funRack = gridfun.initialFunRack()

    #===== printing

    def __str__(self):
        #s = form("Solver({})", self.task.shortStr())
        s = "Solver"
        return s

    #=====

    def getSolver(self) -> 'Solver':
        return self


#---------------------------------------------------------------------

#end
