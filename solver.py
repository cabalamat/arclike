# solver.py = attempts to solve a Task

"""
Solver attempts to solve a task.
"""

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
    loss: int

    tpy: list[Grid] = [] # outputs from the gridFun

    def getSolver(self) -> 'Solver':
        """ go up through my ancestors until we reach the solver """
        return self.parent.getSolver()

    def getTargetOutputs(self) ->  list[Grid]:
        return self.getSolver().targetOutputs

    def getFunRack(self) -> list[GridFun]:
        return self.getSolver().funRack



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

    #=====

    def getSolver(self) -> 'Solver':
        return self


#---------------------------------------------------------------------

#end
