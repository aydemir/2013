#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.configure("--with-lfs")

def build():
    autotools.make()

def install():
    pisitools.dobin("vobcopy")

    pisitools.doman("vobcopy.1")
    pisitools.dodoc("Changelog", "COPYING", "README")
