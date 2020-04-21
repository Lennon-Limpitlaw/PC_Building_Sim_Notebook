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
