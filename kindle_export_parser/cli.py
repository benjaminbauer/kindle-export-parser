import click
import os

# from kindle_export_parser.notebook import KindleNotebook, Note
# from kindle_export_parser.parser import MyHTMLParser
from notebook import KindleNotebook, Note
from parser import MyHTMLParser
from md_renderer import render_md_from_notebook

@click.command()
@click.argument('file')
def convert(file):
    """Kindle Notebook Export to Markdown"""

    test_html_file = file
    f = open(test_html_file, "r", encoding="utf8")
    note = KindleNotebook()
    parser = MyHTMLParser(note)
    parsed = parser.feed(f.read())

    md_string = render_md_from_notebook(note)
    print(md_string)

if __name__ == '__main__':
    convert()

