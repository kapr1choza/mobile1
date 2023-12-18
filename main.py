from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class NoteScreen(Screen):
    def __init__(self, **kwargs):
        super(NoteScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", spacing=10)

        self.note_input = TextInput(hint_text="Введите заметку", multiline=True)
        self.layout.add_widget(self.note_input)

        save_button = Button(text="Сохранить", on_press=self.save_note)
        self.layout.add_widget(save_button)

        list_button = Button(text="Просмотреть заметки", on_press=self.show_notes)
        self.layout.add_widget(list_button)

        self.add_widget(self.layout)

    def save_note(self, instance):
        note_text = self.note_input.text
        if note_text:
            app = App.get_running_app()
            app.notes.append(note_text)
            self.note_input.text = ""

    def show_notes(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "view_notes_screen"


class ViewNotesScreen(Screen):
    def __init__(self, **kwargs):
        super(ViewNotesScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", spacing=10)

        self.notes_label = TextInput(hint_text="Список заметок", multiline=True, readonly=True)
        self.layout.add_widget(self.notes_label)

        back_button = Button(text="Назад", on_press=self.go_back)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def on_enter(self):
        app = App.get_running_app()
        self.notes_label.text = "\n".join(app.notes)

    def go_back(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "note_screen"


class NoteApp(App):
    def build(self):
        self.notes = []
        self.screen_manager = ScreenManager()

        note_screen = NoteScreen(name="note_screen")
        view_notes_screen = ViewNotesScreen(name="view_notes_screen")
        self.screen_manager.add_widget(note_screen)
        self.screen_manager.add_widget(view_notes_screen)

        return self.screen_manager


if __name__ == "__main__":
    NoteApp().run()
