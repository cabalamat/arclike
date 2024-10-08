# solver.py = attempts to solve a Task

"""
Solver attempts to solve a task.
"""

from typing import Union, Optional, Any

from colorist import Color, BrightColor, BgColor, BgBrightColor

from utils import butil
from utils.butil import pr, prn, dpr, form, kv

import grid
from grid import Grid

from problem import Task, Pair

import gridfun
from gridfun import GridFun

from patrec import gridLoss

#---------------------------------------------------------------------
# pretty text for ansi terminals

STARS = BrightColor.WHITE + BgColor.RED + "******"

SOLVED = (BrightColor.WHITE
          + STARS
          + BgColor.GREEN + " SOLVED "
          + STARS
          + BgColor.DEFAULT + Color.DEFAULT)

#---------------------------------------------------------------------
"""
A Node is the result of applying a GridFun to as series of training pair
inputs

Instance variables are:
parent = the node that created this node
solver = the ultimate ancestor odf this node
fun = the gridFun, from (parent) that was used to create this node
children = the nodes expanded from here
"""

class Node:
    parent: 'Node'
    solver: 'Solver'
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
        newNode.solver = self.getSolver()
        newNode.fun = gf
        newNode.calcTpyEtc()
        return newNode

    def calcTpyEtc(self):
        """ For this newly-created node, calculate:
        (self.tpy) = outout from applying (self.fun)
        (self.loss) = loss compasring (self.tpy) with targetOutputs
        """
        dpr("{} enters calcTpyEtc()", self)
        xs: list[Grid] = self.parent.tpy
        self.tpy = [self.fun.run(x)
                    for x in xs]
        dpr(f"xs -> tpy")
        self.loss = 0
        targets: list[Grid] = self.getSolver().targetOutputs
        for ix, x in kv(xs):
            y = self.tpy[ix]
            pr(grid.gridXYAnsi(f"[{ix}]", x, y))
            targ = targets[ix]
            lossYTarg = gridLoss(y, targ)
            prn(f"loss={lossYTarg}")
            self.loss += lossYTarg
        #//for
        exc = SOLVED if self.loss==0 else ""
        dpr(f"self.loss={self.loss} {exc}")


    def __str__(self) -> str:
        s = self.parent.__str__()
        s += "|"
        s += self.fun.__str__()
        return s

    def strWithLoss(self):
        """ return a description string of this Node, similar to __str__
        but with the loss in parentheses after it.
        """
        s = form("%s (%s)", self.__str__(), self.loss)
        return s

    def thisAndDescendents(self) -> list['Node']:
        """ return this node and all its descendents """
        return [self] + self.descendents()

    def descendents(self) -> list['Node']:
        """ return all the nodes descended from this one """
        result = []
        for child in self.children:
            result += child.thisAndDescendents()
        #//for
        return result



class NullNode(Node):
    """ a NullNode is an empy node not used for anything.
    It has one instance, (theNullNode)
    """

theNullNode = NullNode


#---------------------------------------------------------------------
"""
A Solver is the head-node to a Task
"""

class Solver(Node):
    parent: Node = theNullNode
    solver: Node = theNullNode
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

    def __str__(self) -> str:
        #s = form("Solver({})", self.task.shortStr())
        s = "Solver"
        return s

    #=====

    def getSolver(self) -> 'Solver':
        return self


#---------------------------------------------------------------------

#end
