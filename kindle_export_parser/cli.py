import click

from .notebook import KindleNotebook
from .parser import MyHTMLParser
from .md_renderer import render_md_from_notebook


@click.command()
@click.argument('file')
def convert(file):
    """Kindle Notebook Export to Markdown"""

    test_html_file = file
    f = open(test_html_file, "r", encoding="utf8")
    note = KindleNotebook()
    parser = MyHTMLParser(note)
    parser.feed(f.read())

    md_string = render_md_from_notebook(note)
    print(md_string)


if __name__ == '__main__':
    convert()

