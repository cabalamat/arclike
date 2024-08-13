# maketasks.py = make tasks

"""
Make some tasks and save them to disk.
"""


from utils import butil
from utils.butil import prn, dpr, form, join

import problem
from problem import Task, Pair

import gridfun
from gridfun import GridFun

#---------------------------------------------------------------------

def makeFunPairs(fun: GridFun, namePrefix: str, pairData: list[str])
    -> list[Pair]:
    """ make pairs, using (fun) to find the output """
    pairs = []
    for ix, px in butil.kv(parData):
        gx = Grid(px)
        gy = fun.run(gx)
        name = form("{}[{}]", namePrefix, ix)
        pair = Pair(name)
        pair.x = gx
        pair.y = gy
        pairs.append(pair)
    #//for ix, px
    return pairs

#---------------------------------------------------------------------

FT_INDEX = 0

def saveFunTask(inDir: str, name: str, fun: GridFun,
                train: list[str],
                test: list[str]):
    """ create a FunTask and save it to inDir """
    global FT_INDEX
    FT_INDEX += 1
    longName = f"{FT_INDEX:03}_{name}"
    pan = join(inDir, longName + ".json")

    tk = Task(longName)
    tk.train = makeFunPairs(fun, "train", train)
    tk.test  = makeFunPairs(fun, "test",  test)
    tk.saveToFile(pan)

#---------------------------------------------------------------------

saveFunTask("very_easy"


#end
