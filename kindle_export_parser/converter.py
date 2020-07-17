import os

from .notebook import KindleNotebook
from .parser import MyHTMLParser
from .md_renderer import render_md_from_notebook


def convert_kindle_html_to_md(html_file):
    if not os.path.exists(html_file):
        raise ValueError("no such file: " + html_file)

    note = KindleNotebook()
    parser = MyHTMLParser(note)

    with open(html_file, "r", encoding="utf8") as f:
        try:
            parser.feed(f.read())

            return render_md_from_notebook(note)
        except OSError as error:
            print("could not open file for reading: " + error)

