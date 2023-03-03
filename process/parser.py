from .tokens import Parameters, init
from dataclasses import asdict


class Parser:
    def __init__(self, file, path):
        self.gn = file.read().split('\n')
        self.name = path.replace('.gn', '')
        self.param = Parameters()
        self.init()
        self.dump()

    def init(self):
        self.tex = f'{init[1:-1]}'

    def dump(self):
        self.tex = self.tex.format(*asdict(self.param).values())
        with open(f'./{self.name}.tex', 'w+') as file:
            file.write(self.tex)
