from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from .button_utilities import VerifyDeleteButton


class DeleteSaveScreen(Screen):
	def __init__(self,**kwargs):
		super(DeleteSaveScreen, self).__init__(**kwargs)

	def get_saveID(self):
		return self.__saveID

	def build(self, saveID):
		self.__saveID = saveID

		the_label = Label(text='Are you sure you want to delete this save? This cannot be undone!',
		size_hint=(1, 0.7), pos_hint={'x':0, 'y':0.3})

		yes_button = VerifyDeleteButton(0.4/3, 0.1, 'Yes', self.get_saveID())
		no_button = VerifyDeleteButton(2*(0.4/3)+0.3, 0.1, 'No', self.get_saveID())

		self.add_widget(the_label)
		self.add_widget(yes_button)
		self.add_widget(no_button)
