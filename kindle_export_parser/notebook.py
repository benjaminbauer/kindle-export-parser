import re


class KindleNotebook:
    def __init__(self):
        self.bookTitle = None
        self.author = None
        self.sections = []


class Section:
    def __init__(self, title):
        if not isinstance(title, str):
            raise ValueError("'title' needs to be a nonempty string")
        self.chapters = {}
        self.title = title

    def add_note(self, note):
        if not isinstance(note, Note):
            raise ValueError("'note' needs to be a Note")

        self.chapters.setdefault(note.chapter, []).append(note)


class Note:
    def __init__(self, raw_title, text):
        # TODO this needs to be relaxed for bookmarks
        if not isinstance(text, str):
            raise ValueError("'text' needs to be a String")

        if not isinstance(raw_title, str):
            raise ValueError("'raw_title' needs to be a String")

        self.color = Note.colorFromRawTitle(raw_title)
        self.chapter = Note.chapterFromRawTitle(raw_title)
        self.position = Note.positionFromRawTitle(raw_title)
        self.type = Note.typeFromRawTitle(raw_title)

        self.text = text

    @staticmethod
    def colorFromRawTitle(raw_title):
        match = re.search(r'\((.*?)\)', raw_title)
        if match:
            return match.group(1)
        else:
            return 'N/A'

    @staticmethod
    def chapterFromRawTitle(raw_title):
        match = re.search(
            r'^[a-zA-Z \(\)]*\s-\s(.*?)\s>\s[a-zA-Z]*\s([0-9]*?)\s·\s[a-zA-Z]*\s([0-9]*?)$', raw_title)

        if match:
            return match.group(1)
        else:
            return 'N/A'

    @staticmethod
    def positionFromRawTitle(raw_title):
        match = re.search(
            r'[a-zA-Z]*\s([0-9mdclxvi]+?)\s·\s[a-zA-Z]*\s([0-9]*?)$', raw_title)
        if match:
            return match.group(0)
        else:
            raise ValueError("Could not parse position from: '{}'".format(raw_title))

    @staticmethod
    def typeFromRawTitle(raw_title):
        # match 'Higlight(', 'Note ', 'Bookmark '
        match = re.search(r'^([a-zA-Z]*)', raw_title)
        # TODO no error checking yet it it is really on of:
        # ['Bookmark', 'Note', 'Highlight']
        if match:
            return match.group(1)
        else:
            raise ValueError("Could not parse title from: '{}'".format(raw_title))

    @staticmethod
    def _segmentsFromRawTitle(raw_title):
        segments = raw_title.split('-')

        if (len(segments) != 2):
            raise ValueError(
                "unexpected title for parsing chapter: '{}'".format(raw_title))

        return segments
