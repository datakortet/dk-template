import os
import textwrap

from dktemplate.parse import parse

BASEDIR = os.path.dirname(__file__)


def test_simple_repr():
    assert repr(parse("{{ x }}")) == textwrap.dedent("""
    {
        x: {{x}}
    }
    {% program None %} ==> []
        {{ x }} ===> ['x']
    {% endprogram %}""")


def test_include5():
    assert repr(parse("""
    {% include "testdata/include2.html" %}
    """, os.path.join(BASEDIR, 'curdir'))) == textwrap.dedent("""
    {
        include2: {{include2}}
    }
    {% program None %} ==> []

    {% endprogram %}""")
