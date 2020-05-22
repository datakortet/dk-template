import os, re
from dktemplate.render import render

DIRNAME = os.path.dirname(__file__)


# def test_render():
#     fname = os.path.join(DIRNAME, 'testdata', 'for-template.html')
#     template = open(fname).read()
#     # template = re.sub(r'TEMPLATEVARS:.*?:TEMPLATEVARS', "", template)
#     assert render(template, fname) == ''
