from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


Builder.load_file('design.kv')


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.__start_screen = StartScreen('backend/database/saves.db')
