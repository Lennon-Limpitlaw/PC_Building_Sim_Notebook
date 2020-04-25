from kivy.uix.screenmanager import Screen
from backend.database.wrapper import Handler


class NotesScreen(Screen):
	def __init__(self, filename, **kwargs):
		super(NotesScreen, self).__init__(**kwargs)
		self.__handler = Handler(filename)

	def build(self, saveID, page_change=None):
		self.__saveID = saveID
		if page_change is not None:
			self.__page_number += page_change
		else:
			self.__page_number = 0

		notes = self.__handler.select_query('notes', ['saveID = '+str(self.get_saveID()), 'completed = False'])

	def get_saveID(self):
		return self.__saveID
