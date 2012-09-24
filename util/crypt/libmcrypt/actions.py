#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    # Empty
    pisitools.removeDir("/usr/lib/libmcrypt")

    pisitools.dodoc("ChangeLog","COPYING.LIB","KNOWN-BUGS","NEWS","README")
