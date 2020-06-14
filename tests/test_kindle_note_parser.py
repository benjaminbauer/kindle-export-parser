import pytest
from unittest.mock import call
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

def test_section_headings():
    notebook_parsed = run_parser()
    assert len(notebook_parsed.sections) == 2
    #TODO fix assertion
    # assert notebook_parsed.sections == [
    #         'Introduction: My Story',
    #         'The Fundamentals: Why Tiny Changes Make a Big Difference'
    #     ]

#TODO fix mocking
# def test_notes(mocker):
#     mock = mocker.patch('kindle_export_parser.notebook.Note.__init__', return_value=None)
#     mock.patch('kindle_export_parser.notebook.Note.chapter', return_value=None)
#     notebook_parsed = run_parser()
#     notes = []

#     for section in notebook_parsed.sections:
#         for note in section.notes:
#             notes.append(note)

#     assert len(notes) == 3

#     expected_calls = [
#             call('Highlight(yellow) - Page 7 · Location 151', 'the quality of our lives often depends on the quality of our habits.'),
#             call('Highlight(yellow) - 1: The Surprising Power of Atomic Habits > Page 17 · Location 277', 'Making a choice that is 1 percent better or 1 percent worse seems insignificant in the moment, but over the span of moments that make up a lifetime these choices determine the difference between who you are and who you could be.'),
#             call('Highlight(yellow) - 1: The Surprising Power of Atomic Habits > Page 18 · Location 281', 'You should be far more concerned with your current trajectory than with your current results.'),
#         ]

#     mock.assert_has_calls(expected_calls)
