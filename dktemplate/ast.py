# -*- coding: utf-8 -*-
import os
import re

from dktemplate.find_template import find_template
from dktemplate.tokenize import name


class Node(object):
    pass


class Value(Node):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "{{ %s }} ===> %r" % (self.val, list(self.fvars()))

    def fvars(self):
        return {self.val.split('|')[0]}


class Tag(Node):
    def __init__(self, name, content=None, fname=None):
        self.name = name
        self.content = content
        self.fname = fname

    def is_identifier(self, txt):
        return re.match('^[\w\.]+$', txt)

    def find_identifiers(self, txt):
        return set(t for t in txt.split() if self.is_identifier(t))

    def __repr__(self):
        return "{%% %s %s %%} ==> %r" % (self.name, self.content, list(self.fvars()))

    def matches(self, endtag):
        return name(endtag)[3:] == self.name

    def fvars(self):
        return self.find_identifiers(self.content) if self.content else set()

    def dvars(self):
        return set()


class NoOpTag(Tag):
    def __repr__(self):
        return ""

    def fvars(self):
        return set()


class IfTag(Tag):
    def fvars(self):
        return self.find_identifiers(self.content) - {'and', 'or', 'not'}


class ForTag(Tag):
    def fvars(self):
        return self.find_identifiers(self.content.split(' in ', 1)[1])

    def dvars(self):
        implicit = {'forloop', 'forloop0', 'in', 'for'}
        return implicit | self.find_identifiers(self.content.split(' in ', 1)[0])


class WithTag(Tag):
    def fvars(self):
        if ' as ' in self.content:
            return self.find_identifiers(self.content.rsplit(' as ', 1)[0])
        else:
            return self.find_identifiers(self.content.split('=', 1)[1])

    def dvars(self):
        if ' as ' in self.content:
            return {'as'} | self.find_identifiers(self.content.rsplit(' as ', 1)[1])
        else:
            return self.find_identifiers(self.content.split('=', 1)[0])


class IncludeTag(Tag):
    def __repr__(self):
        return ""

    def fvars(self):
        from .parse import parse_file
        path = eval(self.content)
        # if path.startswith('.'):
        #     # this is so the tests can find included files
        #     parentpath = os.path.dirname(self.fname)
        #     childpath = os.path.join(parentpath, path)
        #     path = os.path.abspath(os.path.normpath(childpath))
        #     return parse_file(path).fvars()

        path = find_template(path)
        return parse_file(path).fvars()


class Block(Node):
    def __init__(self, name, tag, block):
        self.name = name
        self.tag = tag
        self.block = block
        self.indent_level = 0

    def indent(self, txt, n):
        return '\n'.join(['    ' * n + line for line in txt.splitlines()])

    def fvars(self):
        res = self.tag.fvars()
        for item in self.block:
            res |= {fv.split('.', 1)[0] for fv in item.fvars()}
        return res - self.dvars() - {'request', 'for', 'as', 'in'}

    def dvars(self):
        return self.tag.dvars()

    def display_fvars(self):
        return "{\n    " + ',\n    '.join(["%s: {{%s}}" % (fv, fv) for fv in self.fvars()]) + '\n}'

    def __repr__(self):
        # print self.fvars()
        block = '\n'.join(repr(s) for s in self.block)
        return "\n%s%s\n%s\n%s\n%s" % (
            self.indent("", self.indent_level),
            self.display_fvars(),
            self.indent(repr(self.tag), self.indent_level),
            self.indent(block, self.indent_level + 1),
            '{%% end%s %%}' % self.name
        )
        # return "\n%sFV: %s\tDV: %s\n%s\n%s\n%s" % (
        #     self.indent("", self.indent_level),
        #     self.display_fvars(),
        #     list(self.tag.dvars()),
        #     self.indent(repr(self.tag), self.indent_level),
        #     self.indent(block, self.indent_level + 1),
        #     '{%% end%s %%}' % self.name
        # )
