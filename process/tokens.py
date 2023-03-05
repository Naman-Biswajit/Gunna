from dataclasses import dataclass

init = (
'''
\\documentclass{{article}}
\\usepackage[{}]{{babel}}
\\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{{geometry}}
{}
\\begin{{document}}
{}
\\end{{document}}
{}
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
    }

    diarg = ['link']

    requires = {
        'href' : ['head', '\\usepackage[colorlinks=true, allcolors=blue]{{hyperref}}\n'],
        'title' : ['body', '\\maketitle\n'],
    }
    
    tags = {'appendix:', 'table-content:'}
    
    tinsert = {
        'appendix:': '\\appendix',
        'table-content:': '\\tableofcontents',
        'table-of-content:': '\\tableofcontents',
    }

    func_aliases = {
        'link' : 'href'
    }

parameters = {
    'lang': 'english',
    'head': '',
    'body': 'Body not found',
    'bibliography':  ''
}
