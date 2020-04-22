from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from backend.database.wrapper import Handler
from .button_utilities import *


class StartScreen(Screen):
	def __init__(self, filename, **kwargs):
		'''Initialises the screen which the user will see when they load in'''
		super(StartScreen, self).__init__(**kwargs)
		self.__handler = Handler(filename)
		self.build()

	def build(self):
		'''Builds the screen with the saves that exist'''
		saves = self.__handler.select_query('*', 'Saves', None)
		save_bars = [None, None, None]

		for save in saves:
			save_bars[save[0]] = save[0]

		for i in range(len(save_bars)):
			if save_bars[i] is not None:
				save_button = SaveButton(0.05, 0.7-i*0.3, 'Save %d'%i, i)
				delete_button = DeleteSaveButton(0.6, 0.7-i*0.3, 'X', i)
				self.add_widget(save_button)
				self.add_widget(delete_button)

			else:
				save_button = CreateSaveButton(0.05, 0.7-i*0.3, 'No Save', i)
				self.add_widget(save_button)

	def delete_save(self, verify, saveID):
		if verify == 'Yes':
			table = 'saves'
			conditions = ['saveID = ' + str(saveID)]

			self.__handler.delete_query(table, conditions)

			self.build()

		else:
			pass

	def create_save(self):
		pass
