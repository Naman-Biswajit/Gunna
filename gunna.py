import sys
from utils.checks import exists
from process.interpreter import Interpreter

# keys = sys.argv
# paths = exists(keys)
paths = ['example.gn']
with open(path := paths[0]) as file:
    Interpreter(file, path)
