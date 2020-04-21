from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from frontend.start_screen import StartScreen
from frontend.delete_save_screen import DeleteSaveScreen


Builder.load_file('design.kv')


class WindowManager(ScreenManager):
	def __init__(self, filename, **kwargs):
		super(WindowManager, self).__init__(**kwargs)
		self.__start_screen = StartScreen(filename)
		self.__delete_save_screen = DeleteSaveScreen()
		self.add_widget(self.__start_screen)
		self.add_widget(self.__delete_save_screen)
		self.current_screen = self.__start_screen


class MyApp(App):
	def __init__(self, **kwargs):
		super(MyApp, self).__init__(**kwargs)

	def build(self):
		self.window = WindowManager('backend/database/saves.db')
		return self.window


if __name__ == '__main__':
	MyApp().run()
