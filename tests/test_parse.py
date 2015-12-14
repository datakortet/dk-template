# -*- coding: utf-8 -*-
import os

from dktemplate.parse import parse

BASEDIR = os.path.dirname(__file__)


def test_value():
    assert parse("{{ a }}").fvars() == {'a'}


def test_if():
    assert parse("""
    {% if a %}
        {{ b }}
    {% elif c == d %}
        {{ e }}
    {% else %}
        {{ f }}
    {% endif %}
    """).fvars() == set('abcdef')


def test_for():
    assert parse(u"""
    {% for a in alist %}
        {{ a }} {{ b }}
    {% endfor %}
    """).fvars() == {'alist', 'b'}


def test_with():
    assert parse("""
    {% with x=foo.bar %}
        {{ x }} {{ y }}
    {% endwith %}
    """).fvars() == {'foo', 'y'}


def test_with2():
    assert parse("""
    {% with foo.bar as x %}
        {{ x }} {{ y }}
    {% endwith %}
    """).fvars() == {'foo', 'y'}


def test_load():
    assert parse("{% load foo %}").fvars() == set()


def test_include():
    assert parse("""
    {% include "./testdata/a-template.html" %}
    """, os.path.join(BASEDIR, 'curdir')).fvars() == {'a'}


def test_include2():
    assert parse("""
    {% for a in alist %}
        {% include "./testdata/a-template.html" %}
    {% endfor %}
    """, os.path.join(BASEDIR, 'curdir')).fvars() == {'alist'}
