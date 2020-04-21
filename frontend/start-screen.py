from kivy.uix.screenmanager import Screen
from .backend.database.wrapper import Handler


class StartScreen(Screen):
    def __init__(self, filename, **kwargs):
        """Initialises the screen which the user will see when they load in"""
        super(StartScreen, self).__init__(**kwargs)
        self.__handler = Handler(filename)
        self.build()

    def build(self):
        saves = self.__handler.select_query('*', 'Saves', None)

        for i in range(len(saves)):
            if saves[i][0] == i:
                save_button = SaveButton(0.05, 0.7-i*0.3, 'Save %d'%i, i)
                delete_button = DeleteSaveButton(0.6, 0.7-i*0.3, 'X', i)
                self.add_widget(save_button)
                self.add_widget(delete_button)

            else:
                save_button = CreateSaveButton(0.05, 0.7-i*0.3, 'No Save', i)
                delete_button = DeleteSaveButton(0.6, 0.7-i*0.3, 'X', i, background_color=(0,0,0,0))
                self.add_widget(save_button)
                self.add_widget(delete_button)
