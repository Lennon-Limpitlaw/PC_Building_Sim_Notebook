from kivy.uix.screenmanager import Screen
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
		self.clear_widgets()
		saves = self.__handler.select_query('*', 'Saves', None)
		save_bars = [None, None, None]

		for save in saves:
			save_bars[save[0]] = save[0]

		for i in range(len(save_bars)):
			if save_bars[i] is not None:
				save_button = SaveButton(0.05, 0.7-i*0.3, 'Save %d\nUsername: %s'%(i+1, saves[i][1]), i)
				delete_button = DeleteSaveButton(0.6, 0.7-i*0.3, 'X', i)
				self.add_widget(save_button)
				self.add_widget(delete_button)

			else:
				save_button = CreateSaveButton(0.05, 0.7-i*0.3, 'No Save', i)
				self.add_widget(save_button)

	def delete_save(self, verify, saveID):
		'''Deletes a specified save with validation'''
		if verify == 'Yes':
			table = 'saves'
			conditions = ['saveID = ' + str(saveID)]

			self.__handler.delete_query(table, conditions)

			self.build()

		else:
			pass

	def create_save(self, saveID, username):
		'''Creates a new save, from a specified save slot and a given username'''
		table = 'saves'
		values = [str(saveID), '\'%s\''%username]

		self.__handler.insert_query(table, values)

		self.build()
