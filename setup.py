"""setup.py - install script for the pandoc-comments filter."""

import re
import io

from setuptools import setup
DESCRIPTION = """A pandoc filter for block comments in markdown documents."""

# From https://stackoverflow.com/a/39671214
__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    io.open('pandoc_comments.py', encoding='utf_8_sig').read()
    ).group(1)

setup(
    name='pandoc-comments',
    version=__version__,

    author='Thomas J. Duck',
    author_email='tomduck@tomduck.ca',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    license='GPL',
    keywords='pandoc comments filter',
    url='https://github.com/tomduck/pandoc-comments',
    download_url='https://github.com/tomduck/pandoc-comments/tarball/' + \
                 __version__,

    install_requires=['pandocfilters>=1.4.2,<2'],

    py_modules=['pandoc_comments'],
    entry_points={'console_scripts':['pandoc-comments = pandoc_comments:main']},

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python'
        ],
)
