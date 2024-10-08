# problem.py  = a Problem

from typing import Union, Optional, Any
import os
import json

from utils import butil
from utils.butil import prn, dpr, form

import grid
from grid import Grid

#---------------------------------------------------------------------

# the directory this file ids in:
PROG_DIR = os.path.dirname(os.path.realpath(__file__))


"""  Python data structures containing JSON data """
JsonValue = Union['JsonObject', 'JsonArray', 'JsonAtom']
JsonObject = dict[str, 'JsonValue']
JsonArray = list['JsonValue']
JsonAtom = Union[str, int, float, bool, None]

#---------------------------------------------------------------------
""" A Pair is a combination of a Grid containing an input (x) and
a Grid containing the corresponding output (y).
"""

class Pair:
    desc: str
    x: Grid
    y: Grid

    def __init__(self, desc: str, jv: Optional[JsonObject] =None):
        self.desc = desc
        if jv:
            self.x = Grid(jv['input'])
            self.y = Grid(jv['output'])

    def __eq__(self, p):
        #dpr("self.x={}", self.x)
        return self.x==p.x and self.y==p.y

    def json(self) -> JsonObject:
        """ return json for this Pair """
        j = {'input':  self.x.g,
             'output': self.y.g
            }
        return j


    #===== pretty output =====

    def ansi(self) -> str:
        """return a string using ansi markup to prettyprint the
        value of the Pair with its training set and tests
        """
        return grid.gridXYAnsi(self.desc, self.x, self.y)


#---------------------------------------------------------------------

class Task:
    name: str
    train: list[Pair]
    test: list[Pair]

    def __init__(self, name:str ="", value:Optional[JsonObject] =None):
        self.name = name
        self.train = []
        self.test = []
        if isinstance(value, dict):
            self.loadFromJson(value)

    def __eq__(self, t):
        #dpr("self.train={}", self.train)
        return self.train==t.train and self.test==t.test

    def loadFromJson(self, jv: JsonObject):
        """ load this Problem from (jv) """
        for i, trainItem in enumerate(jv['train']):
            task = Pair(f"train[{i}]", trainItem)
            self.train += [task]
        for i, testItem in enumerate(jv['test']):
            task = Pair(f"test[{i}]", testItem)
            self.test += [task]

    def loadFromFile(self, pan: str):
        """ (pan) is the pathname to a file containing a json object
        """
        jsonDataStr: str = butil.readFile(pan)
        jsonData: JsonObject = json.loads(jsonDataStr)
        if not self.name:
            self.name = pan
        self.loadFromJson(jsonData)

    def saveToFile(self, pan: str):
        """ (pan) is the pathname to a file containing a json object
        """
        jsonDataStr = json.dumps(self.json(), sort_keys=True)
        butil.writeFile(pan, jsonDataStr)

    def json(self) -> JsonObject:
        """ return JSON for this Task """
        j = { 'train': [p.json() for p in self.train],
              'test':  [p.json() for p in self.test],
            }
        return j


    #===== output =====

    def shortStr(self) -> str:
        """ return a short string describing me """
        return f"Task({self.name})"

    def ansi(self) -> str:
        """return a string using ansi markup to prettyprint the
        value of the Problem with its training set and tests
        """
        result = f"===== {self.name} ----- training:\n"
        for pair in self.train:
            result += pair.ansi() + "\n"
        result += "----- tests:\n"
        for pair in self.test:
            result += pair.ansi() + "\n"
        return result

def makeTask(name: str,
             train: list[tuple[str,str]],
             test: list[tuple[str,str]]) -> Task:
    """ Convenience function for making a task.
    Each Pair is a tuple[str,str], with the 1st str being the
    input, and the 2nd the output.
    The strings use the same notation as grid.gFromStr()
    """
    tk = Task(name)
    tk.train = makePairs("train", train)
    tk.test  = makePairs("test", test)
    return tk

def makeTaskFromFile(dirPan: str, fn: str) -> Task:
    """ Convenience function for making a task from a file.
    tasks are strored in directories under data/
    dirPan = directory pathname
    fn = filename
    """
    tk = Task()
    tk.loadFromFile(butil.join(dirPan, fn))
    tk.name = fn
    return tk

def makePairs(namePrefix: str, pairData: list[tuple[str,str]]) -> list[Pair]:
    """ Make some Pairs, either training pairs or test pairs.
    (namePrefix) is the prefix that goes with each Pair's name
    (px) and (py) are grids, using the same notation as grid.gFromStr()
    """
    pairs = []
    for ix, pxpy in butil.kv(pairData):
        px, py = pxpy
        gx = Grid(px)
        gy = Grid(py)
        name = form("{}[{}]", namePrefix, ix)
        pair = Pair(name)
        pair.x = gx
        pair.y = gy
        pairs.append(pair)
    #//for
    return pairs

#---------------------------------------------------------------------


#end
