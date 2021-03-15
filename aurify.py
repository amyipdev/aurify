#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; at version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY of FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have recieved a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import os

if "--help" in sys.argv or "-h" in sys.argv:
    print("aurify 0.1\n"
          "run without -y to be prompted about package updates\n"
          "run with -y to work automatically\n"
          "report bugs to Amy Parker <enbyamy@gmail.com>\n")
    exit(0)

prompt = True
if "-y" in sys.argv:
    prompt = False

aur_helpers = None
if os.path.exists("/usr/bin/paru"):
    aur_helpers = "paru"
elif os.path.exists("/usr/bin/yay"):
    aur_helpers = "yay"
elif os.path.exists("/usr/bin/yaourt"):
    aur_helpers = "yaourt"
else:
    print("aurify: error: no implemented AUR helper found, make sure it is accessible from /usr/bin")

check = os.popen(f"{aur_helpers} -Qq").read()
pkgs = check.split("\n")
for x in pkgs:
    if not len(x):
        continue
    if x.endswith("-git"):
        continue
    if prompt:
        os.system(f"{aur_helpers} -S {x}-git")
    else:
        os.system(f"{aur_helpers} -S --noconfirm {x}-git")
