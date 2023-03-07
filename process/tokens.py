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
        'itemizer' : 'body',
    }

    diarg = ['href']

    requires = {
        'href' : ['head', '\\usepackage[colorlinks=true, allcolors=blue]{{hyperref}}'],
        'title' : ['body', '\\maketitle'],
        'includegraphics' : ['head', '\\usepackage{{graphicx}}'],
    }
    
    block_func = {'includegraphics', 'itemizer'}

    tags = {'appendix:', 'table-content:', 'center'}
    
    tinsert = {
        'appendix:': '\\appendix',
        'table-content:': '\\tableofcontents',
        'table-of-content:': '\\tableofcontents',
        'center' : '\\centering'
    }

    tarrow = {
        'number' : 'enumerate',
        'bullet' : 'itemize',
    }
    
    func_aliases = {
        'link' : 'href',
        'img' : 'includegraphics',
        'list' : 'itemizer'
    }
    
    s_wrap = ['(', '[', '{', '*', '**', '_']


parameters = {
    'lang': 'english',
    'head': '',
    'body': 'Body not found',
    'bibliography':  ''
}
