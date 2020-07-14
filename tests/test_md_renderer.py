from kindle_export_parser.notebook import KindleNotebook, Section, Note
from kindle_export_parser.md_renderer import render_md_from_notebook


def createMockNotebook():
    raw_title_wo_chapter = 'Highlight(yellow) - Page 7 · Location 151'
    raw_title_w_chapter = 'Highlight(yellow) - 1: The Surprising Power of Atomic Habits > Page 17 · Location 277'
    raw_note_w_chapter = "Note - 1: The Surprising Power of Atomic Habits > Page 17 · Location 2771"

    notebook = KindleNotebook()
    notebook.bookTitle = "Title"
    notebook.author = "Author"
    notebook.sections = [Section("Section 1"), Section("Section 2")]
    notes1 = [
        Note(raw_title_wo_chapter, 'il texto 11'),
        Note(raw_title_w_chapter, 'le text 11'),
        Note(raw_title_w_chapter, 'le text 12'),
        Note(raw_note_w_chapter, 'le text 13'),
    ]
    notes2 = [
        Note(raw_title_wo_chapter, 'il texto 21'),
        Note(raw_title_w_chapter, 'le text 21'),
        Note(raw_title_w_chapter, 'le text 22'),
        Note(raw_note_w_chapter, 'le text 23'),
    ]

    notebook.sections[0].add_note(notes1[0])
    notebook.sections[0].add_note(notes1[1])
    notebook.sections[0].add_note(notes1[2])
    notebook.sections[0].add_note(notes1[3])

    notebook.sections[1].add_note(notes2[0])
    notebook.sections[1].add_note(notes2[1])
    notebook.sections[1].add_note(notes2[2])
    notebook.sections[1].add_note(notes2[3])

    return notebook


expectation = """
# Title
Author: Author
## Section 1
### N/A
> il texto 11
### 1: The Surprising Power of Atomic Habits
> le text 11
> le text 12
le text 13
## Section 2
### N/A
> il texto 21
### 1: The Surprising Power of Atomic Habits
> le text 21
> le text 22
le text 23
"""


def test_render_md():
    notebook = createMockNotebook()
    assert render_md_from_notebook(notebook) == expectation

