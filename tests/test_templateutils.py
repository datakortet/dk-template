# -*- coding: utf-8 -*-
from __future__ import print_function

from dktemplate.templatetags.templateutils import split_lines, remove_comments, \
    Arguments, NO_VALUE


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


def test_no_param():
    args = Arguments(raw_contents=u"name nohelp")
    print("ARGS:", args)
    assert args.nohelp
    assert args.nohelp.value is NO_VALUE
    print("NONAMES:", args.nonames)
    assert args.help.value is False


def test_parse_value():
    args = Arguments(raw_contents=u'''n a=1 b=1.2 c="HELLO" d='WORLD' e=True f=a.b''')
    print("ARGS:", args)
    assert len(args) == 6
    assert args.a.value == 1
    assert args.a.kind == 'int'
    assert args.b.value == 1.2
    assert args.b.kind == 'float'
    assert args.c.value == 'HELLO'
    assert args.c.kind == 'string'
    assert args.d.value == 'WORLD'
    assert args.d.kind == 'string'
    assert args.e.value is True
    assert args.e.kind == 'bool'
    assert args.f.value == ['a', 'b']
    assert args.f.kind == 'dotval'


def test_parse1():
    args = Arguments(raw_contents=u"hello world")
    print("ARGS:", args)
    assert args.tagname == 'hello'
    print("ARGNAMES:", args.argnames)
    assert 'world' in args.argnames


def test_parse2():
    args = Arguments(raw_contents=u"greet hello=world")
    print("ARGS:", args)
    assert args.tagname == 'greet'
    print("ARGNAMES:", args.argnames)
    assert args.argnames['hello'] == 'world'


def test_parse3_align():
    args = Arguments(raw_contents=u"greet |hello=world")
    assert args._find('hello').align == 'left'
    args = Arguments(raw_contents=u"greet hello|=world")
    assert args._find('hello').align == 'right'
    args = Arguments(raw_contents=u"greet |hello|=world")
    assert args._find('hello').align == 'center'


def test_getattr():
    args = Arguments(raw_contents=u"greet |hello=world")
    assert args.hello.align == 'left'
    assert args.hello == args[0] == args._find('hello')
    assert args._find('_hello') is None
    assert args._hello is None
    assert len(args) == 1
    args.pop('hello')
    assert len(args) == 0
