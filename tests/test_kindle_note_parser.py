import os

from kindle_export_parser.notebook import KindleNotebook
from kindle_export_parser.parser import MyHTMLParser


def run_parser():

    test_html_file = os.path.dirname(os.path.abspath(
        __file__)) + "/files/sample-export-simple.html"
    f = open(test_html_file, "r", encoding="utf8")
    note = KindleNotebook()
    parser = MyHTMLParser(note)
    parser.feed(f.read())

    return note


def test_bookTitle():
    assert run_parser().bookTitle == "'Atomic Habits: The life-changing million copy bestseller'"


def test_sections():
    notebook_parsed = run_parser()
    assert len(notebook_parsed.sections) == 2

    actual_titles = []

    for section in notebook_parsed.sections:
        actual_titles.append(section.title)

    assert actual_titles == [
        'Introduction: My Story',
        'The Fundamentals: Why Tiny Changes Make a Big Difference'
    ]

# TODO this is not a proper unitstest


def test_notes():
    notebook_parsed = run_parser()

    notes = []

    for section in notebook_parsed.sections:
        for chapter in section.chapters:
            for note in section.chapters[chapter]:
                notes.append(note)

    assert len(notes) == 4

    texts = []
    for note in notes:
        texts.append(note.text)

    assert texts == [
        'the quality of our lives often depends on the quality of our habits.',
        'This is my note in the same place as a highlight',
        'Making a choice that is 1 percent better or 1 percent worse seems insignificant in the moment, but over the span of moments that make up a lifetime these choices determine the difference between who you are and who you could be.',
        'You should be far more concerned with your current trajectory than with your current results.',
    ]
