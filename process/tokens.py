from dataclasses import dataclass

init = (
'''
\\documentclass{{article}}
\\usepackage[{}]{{babel}}
{}
\\begin{{document}}
{}
\\end{{document}}
{}
'''
)

block = (
'''
\\begin{{{0}}}
{1}
\\end{{{0}}}
'''
)

@dataclass
class Tokens:
    functions = {
        'title': 'head',
        'author': 'head',
        'date' : 'head',
        'section': 'body',
        'subsection': 'body',
        'href' : 'body',
        'includegraphics' : 'body',
    }

    diarg = ['href']

    requires = {
        'href' : ['head', '\\usepackage[colorlinks=true, allcolors=blue]{{hyperref}}'],
        'title' : ['body', '\\maketitle'],
        'includegraphics' : ['head', '\\usepackage{{graphicx}}'],
    }
    
    block_func = {'includegraphics'}

    tags = {'appendix:', 'table-content:'}
    
    tinsert = {
        'appendix:': '\\appendix',
        'table-content:': '\\tableofcontents',
        'table-of-content:': '\\tableofcontents',
    }

    func_aliases = {
        'link' : 'href',
        'img' : 'includegraphics'
    }

parameters = {
    'lang': 'english',
    'head': '',
    'body': 'Body not found',
    'bibliography':  ''
}
