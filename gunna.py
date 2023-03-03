import sys
from utils.checks import exists
from process.parser import Parser

keys = sys.argv
paths = exists(keys)

with open(path := paths[0]) as file:
    Parser(file, path)
