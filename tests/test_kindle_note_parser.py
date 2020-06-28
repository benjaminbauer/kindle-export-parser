import pytest
import os

from kindle_export_parser.notebook import KindleNotebook, Note
from kindle_export_parser.parser import MyHTMLParser

def run_parser():

    test_html_file = os.path.dirname(os.path.abspath(__file__)) + "/files/sample-export-simple.html"
    f = open(test_html_file, "r", encoding="utf8")
    note = KindleNotebook()
    parser = MyHTMLParser(note)
    parsed = parser.feed(f.read())

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

def test_notes():
    notebook_parsed = run_parser()

    notes = []

    for section in notebook_parsed.sections:
        for chapter in section.chapters:
            for note in section.chapters[chapter]:
                notes.append(note)

    assert len(notes) == 3
