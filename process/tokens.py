from dataclasses import dataclass

init = (
    '''
\\documentclass{{article}}
\\usepackage[{}]{{babel}}
\\usepackage[letterpaper,top={},bottom={},left={},right={},marginparwidth={}]{{geometry}}
\\usepackage[colorlinks=true, allcolors=blue]{{hyperref}}
{}
\\begin{{document}}
{}
\\end{{document}}
{}
''')


@dataclass
class Tokens:
    title = '\\title\{{0}\}'


@dataclass
class Parameters:
    lang: str = 'english'
    top: str = '2cm'
    bottom: str = '2cm'
    left: str = '3cm'
    right: str = '3cm'
    marginparwidth: str = '1.75cm'
    packages: str = ''
    body: str = 'Body not found'
    bibliography: str = ''
