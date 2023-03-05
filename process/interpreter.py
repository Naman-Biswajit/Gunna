from .tokens import parameters, init, Tokens, block


class Interpreter:
    def __init__(self, file, path):
        self.gn = file.read().split('\n')
        self.name = path.replace('.gn', '')
        self.param = parameters
        self.tokens = Tokens()
        self.body = ''
        self.head = ''
        self.interpret()

    def interpret(self):
        self.tex = f'{init[1:-1]}'
        self.parse()
        self.tex = self.tex.format(*self.param.values())
        with open(f'./{self.name}.tex', 'w+') as file:
            file.write(self.tex)

    def stand_func(self, func, arg: str, txt=None, optional=''):
        arg = arg.strip(' ')
        insert = f'\\{func}{optional}{{{arg}}}'
        insert += f'{{{txt.strip(" ")}}}' if txt is not None else ''
        return insert

    def block_func(self, func, args):
        if func not in self.tokens.block_func:
            return False

        match func:
            case 'includegraphics':
                args = args.split(',')
                path = args[0]
                if len(args) > 1:
                    caption = f'\\caption{{{args[1]}}}'
                    del args[0:2]
                    optional = ', '.join(args)
                else:
                    arg, optional = '', ''
                
                content = self.stand_func(func, path, optional=f'[{optional.strip(" ")}]')
                content += f'\n{caption}'
                self.body += block.format('figure', content)

        return True

    def process_func(self, arg, func, txt=None):

        aliases = self.tokens.func_aliases
        func = aliases[func] if func in aliases else func

        if func in (r := self.tokens.requires):
            match r[func][0]:
                case 'head': self.head = r[func][1]+ '\n' +self.head
                case 'body': self.body = r[func][1]+ '\n' + self.body

        if self.block_func(func, arg):
            return

        if func in self.tokens.diarg:
            arg, txt = arg.split(',')

        insert = self.stand_func(func, arg, txt)

        match self.tokens.functions[func]:
            case 'head': self.head += insert + '\n'
            case 'body': self.body += insert

    def read(self, line, arg='', func='', is_arg=False):
        words = line.split(' ')
        func_keys = set(self.tokens.functions.keys()).union(
            set(self.tokens.func_aliases.keys()))
        insc = list(set(func_keys).intersection(words))

        for word in words:
            i = words.index(word)
            word = self.tokens.tinsert[word] if word in self.tokens.tags else word
            def aspace(): return word + (' ' if len(words)-1 != i else '')
            if is_arg:
                if word.endswith(']'):
                    word = word[:-1]
                    arg += aspace()
                    is_arg = False
                    self.process_func(arg, func)
                    func, arg = '', ''

                else:
                    arg += aspace()

            elif word in insc:
                words.remove(word)
                func = word

                if (word := words[i]).startswith('['):
                    is_arg = True
                    word = word[1:]

                    if word.endswith(']'):
                        word = word[:-1]
                        words.insert(i+1, ']')

                    arg += aspace()

            else:
                self.body += aspace()

    def parse(self):
        for line in self.gn:
            self.read(line)
            self.body += '\n'

        self.param['head'] = self.head
        self.param['body'] = self.body
