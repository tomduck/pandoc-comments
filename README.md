
pandoc-comments 0.1.0
=====================

*pandoc-comments* is a [pandoc] filter that adds a syntax extension to markdown for block comments.

Python  is required.  Install pandoc-comments using `python setup.py install`.  This can be made available via `pip` on request.

Block comments are declared in markdown documents by using a percent sign (%) at the beginning of a paragraph.  Percent signs may be used on subsequent lines but have no additional effect.  For example, see [demo.md].  Inline comments are not supported.  Comments in YAML metadata are not supported.

Processing [demo.md] with `pandoc -s --filter pandoc-comments` gives output in [md], [pdf], [tex], and [html] formats.  Notice that comments are stripped from all output files.

If you find pandoc-comments useful, then please kindly give it a star [on GitHub].

[pandoc]: http://pandoc.org/
[demo.md]: https://raw.githubusercontent.com/tomduck/pandoc-comments/master/demos/demo.md
[pdf]: https://rawgit.com/tomduck/pandoc-comments/master/demos/out/demo.pdf
[tex]: https://rawgit.com/tomduck/pandoc-comments/master/demos/out/demo.tex
[html]: https://rawgit.com/tomduck/pandoc-comments/master/demos/out/demo.html
[on GitHub]:  https://github.com/tomduck/pandoc-comments
