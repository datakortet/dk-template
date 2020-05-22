
from dktemplate.templatetags.templateutils import split_lines, remove_comments


def test_split_lines():
    txt = """
    hello # world
    """
    assert split_lines(txt) == ['hello']

    txt2 = """
    hello
    """
    assert split_lines(txt2) == ['hello']


def test_split_remove_comments():
    txt = """
    hello # world
    """
    assert remove_comments(txt) == 'hello'

    txt2 = """
    hello
    """
    assert remove_comments(txt2) == 'hello'
