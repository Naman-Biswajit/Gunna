import os
from .terminal import coloured

def exists(keys):
    keys.pop(0)
    
    if len(keys) < 1:
        coloured(255, 0, 0, "Please provide a path to the file to be parsed!")
        exit()

    paths = [x for x in keys if x.endswith('.gn')]

    for path in paths:
        if not os.path.isfile(path):
            coloured(255, 0, 0, f'{path}: Invalid path')
            exit()
    return paths
