import pytest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
# print(path.dirname( path.dirname( path.abspath(__file__) ) ) )
# print(path.dirname( path.abspath(__file__) ))
sys.path.append(path.dirname( path.abspath(__file__) ))
from module_b.mod_b import mod_b1
from config import hel
import os
# from dotenv import load_dotenv, find_dotenv
# from pathlib import Path  # python3 only
# # print(find_dotenv())

# env_path = '.env'
# load_dotenv(find_dotenv())
# print(os.environ['APP_HOST'])

def mod_a1(inp):
    inp1 = mod_b1()
    inp1 += inp 
    return inp1

def mod_a2():
    print("environ here ",os.environ['APP_HOST'])
    return os.environ['APP_HOST']