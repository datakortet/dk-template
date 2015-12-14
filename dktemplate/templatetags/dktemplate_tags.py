# -*- coding: utf-8 -*-


from django import template
from django.template import loader

from dktemplate.parse import parse_file

register = template.Library()


@register.inclusion_tag('dktemplate/freevars.html', takes_context=True)
def freevars(ctx):
    template_fname = ctx['dbg_template_name']
    src, origin = template.loader.find_template(template_fname)
    ast = parse_file(src)

    return {
        'fvars': [dict(name=fv, value=ctx[fv]) for fv in ast.fvars()]
    }
