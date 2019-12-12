import pytest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
# print(path.dirname( path.dirname( path.abspath(__file__) ) ) )
# print(path.dirname( path.abspath(__file__) ))
sys.path.append(path.dirname( path.abspath(__file__) ))
from module_b.mod_b import mod_b1
from config import hel


def mod_a1(inp):
    inp1 = mod_b1()
    inp1 += inp 
    return inp1