from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from backend.database.wrapper import Handler
from .button_utilities import CustomerBar, RequirementsBar, DeadlineBar, CompletedCheckBox, SubmitNoteButton


class NoteScreen(Screen):
    def __init__(self, filename, **kwargs):
        super(NoteScreen, self).__init__(**kwargs)
        self.__handler = Handler(filename)

    def build(self, noteID, saveID):
        self.clear_widgets()
        self.__bars = []

        if saveID is not None:
            self.__saveID = saveID

        if noteID is not None:
            self.__existing = True
            note = self.__handler.select_query('*', 'notes', ['noteID = '+str(noteID)])
            self.__noteID = noteID
            customer = note[2]
            requirements = note[3]
            deadline = note[5]
            completed = note[4]

        else:
            self.__existing = False
            notes = self.__handler.select_query('*', 'notes', None)
            self.__noteID = len(notes)
            customer = ''
            requirements = ''
            deadline = ''
            completed = False

        customer_bar = CustomerBar(0.4, 0.85, customer)
        requirements_bar = RequirementsBar(0.4, 0.5, requirements)
        deadline_bar = DeadlineBar(0.4, 0.35, deadline)
        completed_checkbox = CompletedCheckBox(0.4, 0.2, completed)
        self.__bars.append(customer_bar)
        self.__bars.append(requirements_bar)
        self.__bars.append(deadline_bar)
        self.__bars.append(completed_checkbox)

        for bar in self.__bars:
            self.add_widget(bar)

        self.add_widget(Label(text='Customer: ', pos_hint={'x':0.2, 'y':0.85}, size_hint=(0.2, 0.1)))
        self.add_widget(Label(text='Requirements: ', pos_hint={'x':0.2, 'y':0.7}, size_hint=(0.2, 0.1)))
        self.add_widget(Label(text='Deadline: ', pos_hint={'x':0.2, 'y':0.35}, size_hint=(0.2, 0.1)))
        self.add_widget(Label(text='Completed: ', pos_hint={'x':0.2, 'y':0.2}, size_hint=(0.2, 0.1)))
        self.add_widget(SubmitNoteButton(0.35, 0.05, 'Submit'))

    def submit(self):
        if self.__existing:
            pass

        else:
            pass
