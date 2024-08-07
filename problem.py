# problem.py  = a Problem

from typing import Union, Optional, Any

import grid
from grid import Grid

#---------------------------------------------------------------------

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

    def __init__(self, desc: str, jv: JsonObject):
        self.desc = desc
        self.x = Grid(jv['input'])
        self.y = Grid(jv['output'])

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


    def loadFromJson(self, jv: JsonObject):
        """ load this Problem from (jv) """
        for i, trainItem in enumerate(jv['train']):
            task = Pair(f"train[{i}]", trainItem)
            self.train += [task]
        for i, testItem in enumerate(jv['test']):
            task = Pair(f"test[{i}]", testItem)
            self.test += [task]


    #===== pretty output =====

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



#---------------------------------------------------------------------


#end
