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


parameters = {
    'lang': 'english',
    'top': '2cm',
    'bottom':  '2cm',
    'left': '3cm',
    'right': '3cm',
    'marginparwidth': '1.75cm',
    'head': '',
    'body': 'Body not found',
    'bibliography':  ''
}

keywords = ['title', 'author', 'section', 'subsection']
