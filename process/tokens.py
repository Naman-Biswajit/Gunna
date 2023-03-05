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
    functions = {
        'title': 'head',
        'author': 'head',
        'date' : 'head',
        'section': 'body',
        'subsection': 'body',
    }

    tags = {'appendix:', 'table-content:'}
    tinsert = {
        'appendix:': '\\appendix',
        'table-content:': '\\tableofcontents',
        'table-of-content:': '\\tableofcontents',
    }


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
