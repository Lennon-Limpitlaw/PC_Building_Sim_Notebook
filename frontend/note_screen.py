from kivy.uix.screenmanager import Screen
from backend.database.wrapper import Handler


class NoteScreen(Screen):
    def __init__(self, filename, **kwargs):
        super(NoteScreen, self).__init__(**kwargs)
        self.__handler = Handler(filename)

    def build(self, noteID):
        if noteID is not None:
            note = self.__handler.select_query('notes', ['noteID = '+str(noteID)])

        else:
            pass
