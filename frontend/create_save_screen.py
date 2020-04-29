from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from .gui_utilities import SubmitSaveButton


class CreateSaveScreen(Screen):
	def __init__(self, **kwargs):
		super(CreateSaveScreen, self).__init__(**kwargs)

	def build(self, saveID):
		self.username_bar = TextInput(multiline=False, pos_hint={'x':0.3, 'y':0.55}, size_hint=(0.4, 0.2))
		self.submit_button = SubmitSaveButton(0.3, 0.4, 'Submit', saveID)
		self.add_widget(Label(pos_hint={'x':0.1, 'y':0.55}, size_hint=(0.2, 0.2), text='User:'))
		self.add_widget(self.username_bar)
		self.add_widget(self.submit_button)
