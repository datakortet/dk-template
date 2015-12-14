# -*- coding: utf-8 -*-
"""
Tasks file for pyinvoke.

    inv -l          list available commands
    inv build       build eveything

"""

from invoke import collection  # , ctask as task
from dktasklib import Package
from dktasklib.version import version, upversion


pkg = Package()


# individual tasks that can be run from this project
ns = collection.Collection(
    version,
    upversion,
)
