# problem.py  = a Problem

from typing import Union, Optional, Any
from grid import Grid, gridXYAnsi

#---------------------------------------------------------------------

"""  Python data structures containing JSON data """
JsonValue = Union['JsonObject', 'JsonArray', JsonAtom]
JsonObject = dict[str, 'JsonValue']
JsonArray = list['JsonValue']
JsonAtom = Union[str, int, float, bool, None]

class GridPair:
    x: Grid
    y: Grid

    def __init__(self, jv: JsonObject):
        self.x = Grid(jv['input'])
        self.y = Grid(jv['output'])

class Problem:
    name: str
    train: list[GridPair]
    test: list[GridPair]

    def __init__(self, name:str ="", value:Optional[JsonObject] =None):
        self.name = name
        self.train = []
        self.test = []
        if isinstance(value, JsonObject):
            self.loadFromJson(value)


    def loadFromJson(self, jv: JsonObject):
        """ load this Problem from (jv) """
        for trainItem in jv['train']:
            gp = GridPair(trainItem)
            self.train += [gp]
        for testItem in jv['test']:
            gp = GridPair(testItem)
            self.test += [gp]


    #===== pretty output =====

    def ansi(self) -> str:
        """return a string using ansi markup to prettyprint the
        value of the Problem with its training set and tests
        """



#---------------------------------------------------------------------


#end
