from .tokens import parameters, init, keywords


class Parser:
    def __init__(self, file, path):
        self.gn = file.read().split('\n')
        self.name = path.replace('.gn', '')
        self.param = parameters
        self.body = ''
        self.init()
        self.parse_body()
        self.dump()

    def init(self):
        self.tex = f'{init[1:-1]}'

    def dump(self):
        self.tex = self.tex.format(*self.param.values())
        with open(f'./{self.name}.tex', 'w+') as file:
            file.write(self.tex)

    def command(self, arg, tag: list):
        print(arg)

    def parse_body(self, arg=str(), tag=[], is_arg=False):

        for line in self.gn:
            words = line.split(' ')
            insc = list(set(keywords).intersection(words))

            for word in words:
                # check for ignoring symbol
                if is_arg:
                    if word.endswith(']'):
                        arg += word[:-1] + ' '
                        is_arg = False
                        self.command(arg, tag)
                        arg = str()
                        tag.clear()

                    else:
                        arg += word + ' '

                    continue

                if word in insc:
                    i = words.index(word)
                    words.remove(word)
                    tag.extend((word, i, self.gn.index(line)))

                    if (word := words[i]).startswith('['):
                        is_arg = True
                        word = word.replace('[', '')
                        arg += word + ' '

                else:
                    self.body += word + ' '

        self.param['body'] = self.body
