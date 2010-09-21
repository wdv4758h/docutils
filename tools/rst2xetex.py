#!/usr/bin/env python
# .. coding: utf8

# $Id$
# Author: Günter Milde
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing XeLaTeX source code.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline

description = ('Generates XeLaTeX documents from standalone reStructuredText '
               'sources. '
               'Reads from <source> (default is stdin) and writes to '
               '<destination> (default is stdout).  See '
               '<http://docutils.sourceforge.net/docs/user/latex.html> for '
               'the full reference.')

publish_cmdline(writer_name='xetex', description=description)
