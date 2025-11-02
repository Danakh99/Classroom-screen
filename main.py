# -------------------------------
# Smart Table App (Main Entry)
# -------------------------------

from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'resizable', False)
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition

# Screens
from features.main_menu import MainMenu          # Arabic main menu
from features.notebook import NotebookScreen     # دفتر الملاحظات
from features.quiz_math import QuizScreen        # الرياضيات
from features.science import ScienceScreen       # placeholder: العلوم
from features.placeholder import PlaceholderScreen
from features.contact import ContactScreen


class SmartTableApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())

        # Main menu
        sm.add_widget(MainMenu(name='main'))

        # Core features
        sm.add_widget(NotebookScreen(name='notebook'))
        sm.add_widget(QuizScreen(name='quiz'))        # الرياضيات
        sm.add_widget(ScienceScreen(name='science'))  # placeholder science page for now

        # Placeholder subjects
        sm.add_widget(PlaceholderScreen("اللغة الإنجليزية", name='english'))
        sm.add_widget(PlaceholderScreen("الاجتماعيات", name='social'))
        sm.add_widget(PlaceholderScreen("الحاسوب", name='computer'))

        # Contact screen
        sm.add_widget(ContactScreen(name='contact'))

        return sm


if __name__ == '__main__':
    SmartTableApp().run()

