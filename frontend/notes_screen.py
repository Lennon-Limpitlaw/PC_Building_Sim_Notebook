from kivy.uix.screenmanager import Screen
from backend.database.wrapper import Handler
from .gui_utilities import NoteButton, NextButton, PrevButton, BackButton, NewNoteButton


class NotesScreen(Screen):
	def __init__(self, filename, **kwargs):
		super(NotesScreen, self).__init__(**kwargs)
		self.__handler = Handler(filename)

	def build(self, saveID=None, page_change=None):
		self.clear_widgets()
		if saveID is not None:
			self.__saveID = saveID

		if page_change is not None:
			self.__page_number += page_change
		else:
			self.__page_number = 0

		notes = self.__handler.select_query('*', 'notes', ['saveID = '+str(self.get_saveID()), 'completed = 0'])

		note_num = self.__page_number * 6
		count = 0
		for i in range(6):
			try:
				text = 'Customer: %s\nDeadline: %s' % (notes[note_num][2], str(notes[note_num][5]))
				the_note_button = NoteButton(0.1+(i//3)*0.45, (0.7-(i%3)*0.3), text, notes[note_num][0])
				self.add_widget(the_note_button)
				note_num += 1
				count += 1
			except:
				break

		if len(notes) > (self.__page_number+1) * 6:
			next_button = NextButton(0.9, 0, 'Next')
			self.add_widget(next_button)

		if self.__page_number > 0:
			prev_button = PrevButton(0, 0, 'Prev')
			self.add_widget(prev_button)

		back_button = BackButton(0, 0.95, 'Back')
		self.add_widget(back_button)
		new_note_button = NewNoteButton(0.9, 0.95, 'New')
		self.add_widget(new_note_button)

	def get_saveID(self):
		return self.__saveID
