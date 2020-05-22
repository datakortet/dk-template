import os
from dktemplate.templatevars import main

DIRNAME = os.path.dirname(__file__)


def test_templatevars_main():
    assert main(os.path.join(DIRNAME, 'testdata', 'for-template.html'))
