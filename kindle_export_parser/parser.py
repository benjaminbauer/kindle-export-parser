from html.parser import HTMLParser
from .notebook import Section, Note


class MyHTMLParser(HTMLParser):

    def __init__(self, kindleNotebook):
        super().__init__()
        self.kindleNotebook = kindleNotebook

        # bookTitle
        self.lookingAtTitle = False

        self.lookingAtSectionHeading = False
        self.currentSection = None

        # noteHeading
        self.lookingAtNoteHeading = False
        self.lookingAtNoteText = False
        self.tmpNote = {'title': '', 'text': ''}

        # authors
        self.lookingAtAuthor = False

    def handle_starttag(self, tag, attrs):
        if(tag == "div"):
            for att in attrs:
                if(att[0] != 'class'):
                    continue

                if(att[1] == 'bookTitle'):
                    self.lookingAtTitle = True
                elif(att[1] == 'sectionHeading'):
                    # reset the current section if any
                    self.currentSection = None
                    self.lookingAtSectionHeading = True
                elif(att[1] == 'noteHeading'):
                    self.lookingAtNoteHeading = True
                    self.tmpNote = {'title': '', 'text': ''}
                elif(att[1] == 'noteText'):
                    self.lookingAtNoteText = True

    def handle_endtag(self, tag):
        self.lookingAtTitle = False
        self.lookingAtSectionHeading = False

        if self.lookingAtNoteHeading:
            if tag != 'span':
                # there is a <span> in the noteheading
                self.lookingAtNoteHeading = False
        if self.lookingAtNoteText:
            # flush the collected data in tmpNote
            note = Note(self.tmpNote['title'], self.tmpNote['text'])
            self.currentSection.add_note(note)
            self.lookingAtNoteText = False

    def handle_data(self, data):
        if self.lookingAtTitle:
            # title has newlines
            a_string = data.strip()
            literal_string = repr(a_string)
            self.kindleNotebook.bookTitle = literal_string
        elif self.lookingAtSectionHeading:
            self.currentSection = Section(data.strip())
            self.kindleNotebook.sections.append(self.currentSection)
        elif self.lookingAtNoteHeading:
            self.tmpNote['title'] += data.strip()
        elif self.lookingAtNoteText:
            self.tmpNote['text'] += data.strip()
