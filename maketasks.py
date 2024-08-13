# maketasks.py = make tasks

"""
Make some tasks and save them to disk.
"""


from utils import butil
from utils.butil import prn, dpr, form, join

from grid import Grid

import problem
from problem import Task, Pair

import gridfun
from gridfun import GridFun, Rotc, Rotc2, Rotc3, Compress

#---------------------------------------------------------------------

def makeFunPairs(fun: GridFun, namePrefix: str, pairData: list[str])\
    -> list[Pair]:
    """ make pairs, using (fun) to find the output """
    pairs = []
    for ix, px in butil.kv(pairData):
        gx = Grid(px)
        gy = fun.run(gx)
        name = form("{}[{}]", namePrefix, ix)
        pair = Pair(name)
        pair.x = gx
        pair.y = gy
        pairs.append(pair)
    #//for ix, px
    return pairs

FT_INDEX = 0

def saveFunTask(inDir: str, name: str, fun: GridFun,
                train: list[str],
                test: list[str]):
    """ create a FunTask and save it to inDir """
    global FT_INDEX
    FT_INDEX += 1
    longName = f"{FT_INDEX:03}_{name}"
    pan = join("data", inDir, longName + ".json")

    tk = Task(longName)
    tk.train = makeFunPairs(fun, "train", train)
    tk.test  = makeFunPairs(fun, "test",  test)
    tk.saveToFile(pan)

#---------------------------------------------------------------------
"""
Now we've save all our tasks, print them
"""

def printTasks():
    dataDir = join("data", "very_easy")
    fileNames = butil.getFilenames(dataDir, "*.json")
    for fn in fileNames:
        tk = Task()
        tk.loadFromFile(join("data", "very_easy", fn))
        prn(tk.ansi())
        _ = input("next?")
    #//for fn

#---------------------------------------------------------------------

saveFunTask("very_easy", "RotateClockwise", Rotc(),
    ["..12../.3344./..56..",
     "123./456./789.",
     "66667/....7/....7/...77"],
    ["..../1234/5678/...."]
)
saveFunTask("very_easy", "RotateClockwise2", Rotc2(),
    ["..12../.3344./..56..",
     "123./456./789.",
     "66667/....7/....7/...77"],
    ["..../1234/5678/...."]
)
saveFunTask("very_easy", "RotateClockwise3", Rotc3(),
    ["..12../.3344./..56..",
     "123./456./789.",
     "66667/....7/....7/...77"],
    ["..../1234/5678/...."]
)
saveFunTask("very_easy", "Compress", Compress(),
    ["..12../.3344./..56..",
     "123./456./789.",
     "66667/....7/....7/...77"],
    ["..../1234/5678/...."]
)



printTasks()

#end
