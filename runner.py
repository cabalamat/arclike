# runner.py

"""
Solves a series of problems on disk
"""

from utils.butil import join, prn, dpr, form, kv
import problem
from problem import Task
from solver import Node, Solver

#---------------------------------------------------------------------

def run1(dirPan: str, fn: str):
    """ Solve a task defined by (dirPan) and (fn), by expanding the
    root node by 1-ply.
    Write to stdout.
    dirPan = directory to find task files
    fn = the task filename
    """
    tk = problem.makeTaskFromFile(dirPan, fn)
    solv = Solver(tk)
    solv.expand()
    allNodes = solv.thisAndDescendents()

    # all nodes, minimum loss 1st
    nodesByLoss = sorted(allNodes, key=lambda n: n.loss)
    prn("Nodes by increasing loss:")
    for ix, n in kv(nodesByLoss):
        prn("%s. %s", ix, n)
        prn("    %s", n.strWithLoss())

    #//for



#---------------------------------------------------------------------


if __name__=='__main__':
    run1("data/very_easy", "001_RotateClockwise.json")

#end
