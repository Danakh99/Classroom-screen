# features/contact.py

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from features.ui import arabic_label, rounded_btn, BACKGROUND, YELLOW
import webbrowser

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        layout.add_widget(arabic_label("تواصل معنا", 56, {'center_x':0.5, 'top':0.90}))

        self.contact_url = "https://forms.gle/YOUR_LINK_HERE"

        layout.add_widget(rounded_btn(
            "فتح نموذج التواصل",
            {'center_x':0.5,'center_y':0.60}, (0.40,0.12), YELLOW, 30,
            cb=lambda *_: webbrowser.open(self.contact_url)
        ))

        # Back bottom-left (never exits)
        layout.add_widget(rounded_btn(
            "رجوع", {'x':0.05,'y':0.03}, (0.22,0.09), YELLOW, 28,
            cb=lambda *_: setattr(self.manager,'current','mainmenu')
        ))

    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

