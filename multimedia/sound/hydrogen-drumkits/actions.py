#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/hydrogen/data/demo_songs", "demo_songs/*")
    pisitools.insinto("/usr/share/hydrogen/data/drumkits", "drumkits/*")
