#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("CXXFLAGS", "%s -I/usr/include/openjpeg-1.5" % get.CXXFLAGS())

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-poppler-qt \
                         --disable-gtk-doc-html \
                         --disable-zlib \
                         --disable-gtk-test \
                         --enable-poppler-qt4 \
                         --enable-cairo-output \
                         --enable-xpdf-headers \
                         --enable-libjpeg \
                         --enable-libopenjpeg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
