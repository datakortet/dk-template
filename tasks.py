# -*- coding: utf-8 -*-
"""
Tasks file for pyinvoke.

    inv -l          list available commands
    inv build       build eveything

"""

from invoke import ctask as task, collection
from dktasklib import Package, collectstatic
from dktasklib.version import version, upversion


pkg = Package()


# individual tasks that can be run from this project
ns = collection.Collection(
    version,
    upversion,
)
