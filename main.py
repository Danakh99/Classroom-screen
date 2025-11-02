# -------------------------------
# Smart Table App (Main Entry)
# -------------------------------

from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'resizable', False)
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition

from features.main_menu import WelcomeScreen, MainMenu
from features.notebook import NotebookScreen
from features.quiz_math import QuizScreen
from features.science import ScienceScreen
from features.placeholder import PlaceholderScreen
from features.contact import ContactScreen
from features.science.ecosystem import EcosystemScreen




class SmartTableApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())

        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(MainMenu(name='mainmenu'))

        sm.add_widget(NotebookScreen(name='notebook'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ScienceScreen(name='science'))
        sm.add_widget(EcosystemScreen(name="ecosystem"))


        sm.add_widget(PlaceholderScreen(name='english'))
        sm.add_widget(PlaceholderScreen(name='computer'))
        sm.add_widget(PlaceholderScreen(name='social'))

        sm.add_widget(ContactScreen(name='contact'))

        return sm


if __name__ == '__main__':
    SmartTableApp().run()

