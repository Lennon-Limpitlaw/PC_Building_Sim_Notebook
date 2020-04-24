from kivy.uix.screenmanager import Screen
from .button_utilities import SubmitSaveButton


class CreateSaveScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateSaveScreen, self).__init__(**kwargs)

    def build(self, saveID):
        pass
