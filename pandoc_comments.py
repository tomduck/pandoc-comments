#!/usr/bin/env python3

"""pandoc_comments.py - A pandoc filter for block comments in markdown."""

__version__ = '0.1.0'

# Copyright 2019 Thomas J. Duck.
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from pandocfilters import toJSONFilter
from pandocfilters import Null


# pylint: disable=unused-argument
def action(k, v, fmt, meta):
    """Processes elements."""

    if k == 'Para':

        # Comments begin with a %
        if v[0]['t'] == 'Str' and v[0]['c'] and v[0]['c'][0] == '%':
            return []

    return None


def main():
    """Main program."""
    toJSONFilter(action)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
