#!/usr/bin/env python3

"""pandoc_comments.py - A pandoc filter for block comments in markdown."""


import sys

from pandocfilters import toJSONFilter
from pandocfilters import Para


# pylint: disable=unused-argument
def action(k, v, fmt, meta):
    """Processes pandoc AST element with given key (k), value (v), output
    format (fmt) and document metadata (meta)."""

    if k == 'Para':

        # Comments begin with a %
        if v[0]['t'] == 'Str' and len(v[0]['c']) and v[0]['c'][0] == '%':
            return Para([])

    return None


def main():
    """Main program."""
    toJSONFilter(action)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
