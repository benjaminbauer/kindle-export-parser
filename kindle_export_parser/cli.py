import click

import kindle_export_parser.converter as converter


@click.command()
@click.argument('file')
def convert(file):
    """Kindle Notebook Export to Markdown"""
    md_string = converter.convert_kindle_html_to_md(file)
    print(md_string)


if __name__ == '__main__':
    convert()

