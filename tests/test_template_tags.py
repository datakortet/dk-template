import os
from dktemplate.templatetags.dktemplate_tags import freevars

DIRNAME = os.path.dirname(__file__)


class Context(dict):
    def __init__(self, *args, **kw):
        super(Context, self).__init__(*args, **kw)
        self.__dict__ = self



def test_freevars():
    context = Context({
        'dbg_template_name': os.path.join(DIRNAME, 'testdata', 'for-template.html')
    })
    context.dicts = []

    fv = [d['name'] for d in freevars(context)['fvars']]
    assert fv == ['alist', 'b', 'c', 'd', 'e', 'f']
