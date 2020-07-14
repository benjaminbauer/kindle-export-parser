import pytest
from kindle_export_parser.notebook import Note

raw_title_wo_chapter = 'Highlight(yellow) - Page 7 · Location 151'
raw_title_w_chapter = 'Highlight(yellow) - 1: The Surprising Power of Atomic Habits > Page 17 · Location 277'
raw_title_minus_in_title = 'Highlight(yellow) - 7: The Secret to Self-Control > Page 92 · Location 1275'
raw_title_chapter_one_digit = 'Highlight(blue) - 1 > Page 236 · Location 3354'
raw_title_note = 'Note - 1 > Page 237 · Location 3378'
raw_title_bookmark = 'Bookmark - 2 > Page 242 · Location 3447'
valid_text = 'lorem impsum'
invalid_text_type = 23
invalid_raw_title_type = 23


def test_init_check_text_type():
    with pytest.raises(ValueError):
        Note(raw_title_w_chapter, invalid_text_type)


def test_init_check_raw_title():
    with pytest.raises(ValueError):
        Note(invalid_raw_title_type, valid_text)


@pytest.mark.parametrize("test_input,expected", [
    (raw_title_wo_chapter, "yellow"),
    (raw_title_w_chapter, "yellow"),
    (raw_title_minus_in_title, "yellow"),
    (raw_title_note, "N/A"),
    (raw_title_bookmark, "N/A"),
])
def test_color(test_input, expected):
    assert Note(test_input, valid_text).color == expected


@pytest.mark.parametrize("test_input,expected", [
    (raw_title_wo_chapter, "N/A"),
    (raw_title_w_chapter, "1: The Surprising Power of Atomic Habits"),
    (raw_title_minus_in_title, "7: The Secret to Self-Control"),
    (raw_title_chapter_one_digit, "1"),
    (raw_title_note, "1"),
    (raw_title_bookmark, "2"),
])
def test_chapter(test_input, expected):
    assert Note(test_input, valid_text).chapter == expected


@pytest.mark.parametrize("test_input,expected", [
    (raw_title_wo_chapter, "Page 7 · Location 151"),
    (raw_title_w_chapter, "Page 17 · Location 277"),
    (raw_title_minus_in_title, "Page 92 · Location 1275"),
    (raw_title_note, "Page 237 · Location 3378"),
    (raw_title_bookmark, "Page 242 · Location 3447"),
])
def test_postion(test_input, expected):
    assert Note(test_input, valid_text).position == expected


@pytest.mark.parametrize("test_input,expected", [
    (raw_title_wo_chapter, "Highlight"),
    (raw_title_w_chapter, "Highlight"),
    (raw_title_minus_in_title, "Highlight"),
    (raw_title_note, "Note"),
    (raw_title_bookmark, "Bookmark"),
])
def test_type(test_input, expected):
    assert Note(test_input, valid_text).type == expected

