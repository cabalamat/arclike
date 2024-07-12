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
""" A Task is a combination of a Grid containing an input (x) and
a Grid containimng tyhe correspinding output (y).
"""

class Task:
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
        value of the Task with its training set and tests
        """
        return grid.gridXYAnsi(self.desc, self.x, self.y)


#---------------------------------------------------------------------

class Problem:
    name: str
    train: list[Task]
    test: list[Task]

    def __init__(self, name:str ="", value:Optional[JsonObject] =None):
        self.name = name
        self.train = []
        self.test = []
        if isinstance(value, dict):
            self.loadFromJson(value)


    def loadFromJson(self, jv: JsonObject):
        """ load this Problem from (jv) """
        for i, trainItem in enumerate(jv['train']):
            task = Task(f"train[{i}]", trainItem)
            self.train += [task]
        for i, testItem in enumerate(jv['test']):
            task = Task(f"test[{i}]", testItem)
            self.test += [task]


    #===== pretty output =====

    def ansi(self) -> str:
        """return a string using ansi markup to prettyprint the
        value of the Problem with its training set and tests
        """
        result = f"===== {self.name} ----- training:\n"
        for task in self.train:
            result += task.ansi() + "\n"
        result += "----- tests:\n"
        for task in self.test:
            result += task.ansi() + "\n"
        return result



#---------------------------------------------------------------------


#end
