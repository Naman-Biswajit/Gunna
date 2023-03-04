from .tokens import parameters, init, Tokens


class Parser:
    def __init__(self, file, path):
        self.gn = file.read().split('\n')
        self.name = path.replace('.gn', '')
        self.param = parameters
        self.tokens = Tokens()
        self.body = str()
        self.head = str()
        self.init()
        self.parse_body()
        self.dump()

    def init(self):
        self.tex = f'{init[1:-1]}'

    def dump(self):
        self.tex = self.tex.format(*self.param.values())
        with open(f'./{self.name}.tex', 'w+') as file:
            file.write(self.tex)

    def command(self, arg, func: list):
        self.head += f'\\{func[0]}{{{arg}}}\n'

        match func[0]:
            case 'title':
                self.body = '\\makehead\n' + self.body

    def read(self, line, arg=str(), func=[], is_arg=False):
        words = line.split(' ')
        insc = list(self.tokens.functions.intersection(words))

        for word in words:
            word = self.tokens.tinsert[word] if word in self.tokens.tags else word
            if is_arg:
                if word.endswith(']'):
                    arg += word[:-1] + ' '
                    is_arg = False
                    self.command(arg, func)
                    arg = str()
                    func.clear()

                else:
                    arg += word + ' '

            elif word in insc:
                i = words.index(word)
                words.remove(word)
                func.extend((word, i, self.gn.index(line)))

                if (word := words[i]).startswith('['):
                    is_arg = True
                    word = word.replace('[', '')
                    arg += word + ' '

            else:
                self.body += word + ' '

    def parse_body(self):
        for line in self.gn:
            self.read(line)
            self.body += '\n'

        self.param['body'] = self.body
        self.param['head'] = self.head
