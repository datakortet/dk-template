# -*- coding: utf-8 -*-

"""Test that all modules are importable.
"""

import dktemplate.ast
import dktemplate.find_template
import dktemplate.parse
import dktemplate.render
import dktemplate.templatetags
import dktemplate.templatetags.dktemplate_tags
import dktemplate.templatevars
import dktemplate.tokenize


def test_import_():
    "Test that all modules are importable."
    
    assert dktemplate.ast
    assert dktemplate.find_template
    assert dktemplate.parse
    assert dktemplate.render
    assert dktemplate.templatetags
    assert dktemplate.templatetags.dktemplate_tags
    assert dktemplate.templatevars
    assert dktemplate.tokenize
