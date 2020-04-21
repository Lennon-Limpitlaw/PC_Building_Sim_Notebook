from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from frontend.start_screen import StartScreen


Builder.load_file('design.kv')


class WindowManager(ScreenManager):
    def __init__(self, filename, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.__start_screen = StartScreen(filename)
        self.add_widget(self.__start_screen)


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

    def build(self):
        return WindowManager('backend/database/saves.db')


if __name__ == '__main__':
    MyApp().run()
