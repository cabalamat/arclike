# test_infra.py  = test infrastructure

"""
Tests the infrastructure of gridlike, i.e. everything except the
AI that solves the problem.
"""

from utils import lintest

#---------------------------------------------------------------------

group = lintest.TestGroup()

import test_textblock
group.add(test_textblock.group)

import test_grid
group.add(test_grid.group)

import test_problem
group.add(test_problem.group)

import test_gridfun
group.add(test_gridfun.group)

if __name__=='__main__': group.run()

#end
