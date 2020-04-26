from kivy.uix.button import Button


class SaveButton(Button):
	def __init__(self, x, y, text, saveID, **kwargs):
		super(SaveButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text
		self.__saveID = saveID

	def get_saveID(self):
		return self.__saveID


class CreateSaveButton(Button):
	def __init__(self, x, y, text, saveID, **kwargs):
		super(CreateSaveButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text
		self.__saveID = saveID

	def get_saveID(self):
		return self.__saveID


class DeleteSaveButton(Button):
	def __init__(self, x, y, text, saveID, **kwargs):
		super(DeleteSaveButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text
		self.__saveID = saveID

	def get_saveID(self):
		return self.__saveID


class VerifyDeleteButton(Button):
	def __init__(self, x, y, text, saveID, **kwargs):
		super(VerifyDeleteButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text
		self.__saveID = saveID

	def get_saveID(self):
		return self.__saveID


class SubmitSaveButton(Button):
	def __init__(self, x, y, text, saveID, **kwargs):
		super(SubmitSaveButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text
		self.__saveID = saveID

	def get_saveID(self):
		return self.__saveID


class NoteButton(Button):
	def __init__(self, x, y, text, noteID, **kwargs):
		super(NoteButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text
		self.__noteID = noteID

	def get_noteID(self):
		return self.__noteID


class NextButton(Button):
	def __init__(self, x, y, text, **kwargs):
		super(NextButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text


class PrevButton(Button):
	def __init__(self, x, y, text, **kwargs):
		super(PrevButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text


class BackButton(Button):
	def __init__(self, x, y, text, **kwargs):
		super(BackButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text


class NewNoteButton(Button):
	def __init__(self, x, y, text, **kwargs):
		super(NewNoteButton, self).__init__(**kwargs)
		self.pos_hint = {'x':x, 'y':y}
		self.text = text
