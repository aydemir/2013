#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DBoost_USE_MULTITHREAD=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

    # Move examples under doc dir
    pisitools.domove("usr/share/player/examples", "usr/share/doc/" + get.srcNAME())
