
pandoc-comments 0.1.0
=====================

*pandoc-comments* is a [pandoc] filter that adds a syntax extension to markdown for block comments.  Python  is required.

Block comments are denoted by using a percent sign (%) at the beginning of a paragraph.  For example, see [demo.md].

Processing [demo.md] with `pandoc -s --filter pandoc-comments` gives output in [md], [pdf], [tex], and [html] formats.  Notice that comments are stripped from all output files.

If you find pandoc-comments useful, then please kindly give it a star [on GitHub].

[pandoc]: http://pandoc.org/
[demo.md]: https://raw.githubusercontent.com/tomduck/pandoc-lettrine/master/demos/demo.md
[pdf]: https://rawgit.com/tomduck/pandoc-lettrine/master/demos/out/demo.pdf
[tex]: https://rawgit.com/tomduck/pandoc-lettrine/master/demos/out/demo.tex
[html]: https://rawgit.com/tomduck/pandoc-lettrine/master/demos/out/demo.html
[on GitHub]:  https://github.com/tomduck/pandoc-lettrine
