# -*- coding: utf-8 -*-

from django import template

from dktemplate.find_template import find_template
from dktemplate.parse import parse_file

register = template.Library()


@register.inclusion_tag('dktemplate/freevars.html', takes_context=True)
def freevars(context):
    template_fname = context['dbg_template_name']
    try:
        tmpl_path = find_template(template_fname)
        ast = parse_file(tmpl_path)
        return {
            'fvars': [dict(name=fv, value=context.get(fv, "[MISSING]")) for fv in ast.fvars()]
        }
    except IOError:
        return {
            'fvars': [{'name': 'NOTHING', 'value': 'FOUND'}]
        }
