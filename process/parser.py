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
        insert = f'\\{func[0]}{{{arg}}}'.strip() + '\n'
        if self.tokens.functions[func[0]] == 'head':
            self.head += insert
        else:
            self.body += insert

        match func[0]:
            case 'title':
                self.body = '\\makehead\n' + self.body
    
    def read(self, line, arg=str(), func=[], is_arg=False):
        words = line.split(' ')
        insc = list(set(self.tokens.functions.keys()).intersection(words))
        for word in words:
            i = words.index(word)
            word = self.tokens.tinsert[word] if word in self.tokens.tags else word
            if is_arg:
                if word.endswith(']'):
                    word = word.replace(']', '')
                    arg += word + (' ' if len(words)-1 == i else '')
                    is_arg = False
                    self.command(arg, func)
                    arg = str()
                    func.clear()

                else:
                    arg += word + ' '

            elif word in insc:
                words.remove(word)
                func.extend((word, i, self.gn.index(line)))

                if (word := words[i]).startswith('['):
                    is_arg = True
                    word = word.replace('[', '')
                    
                    if word.endswith(']'):
                        word = word.replace(']', '')
                        words.insert(i+1, ']')
                    
                    arg += word + ' '

            else:
                self.body += word + ' '

    def parse_body(self):
        for line in self.gn:
            self.read(line)
            self.body += '\n'

        self.param['head'] = self.head
        self.param['body'] = self.body
