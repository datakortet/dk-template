# -*- coding: utf-8 -*-

"""Test that all modules are importable.
"""

import dk-template.ast
import dk-template.find_template
import dk-template.parse
import dk-template.render
import dk-template.templatetags
import dk-template.templatetags.dktemplate_tags
import dk-template.templatevars
import dk-template.tokenize


def test_import_():
    "Test that all modules are importable."
    
    assert dk-template.ast
    assert dk-template.find_template
    assert dk-template.parse
    assert dk-template.render
    assert dk-template.templatetags
    assert dk-template.templatetags.dktemplate_tags
    assert dk-template.templatevars
    assert dk-template.tokenize
