#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --enable-pam \
                         --disable-rpath \
                         --disable-device-hal \
                         --disable-mount-hal \
                         --enable-mount-udisks \
                         --enable-mount-eeze \
                         --disable-illume2")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/enlightenment/data/themes/","%s/*.edj" % get.workDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")
