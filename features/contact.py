# features/contact.py

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from features.ui import arabic_label, rounded_btn, BACKGROUND
from kivy.graphics import Color, Rectangle
import webbrowser

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        layout = FloatLayout()

        layout.add_widget(arabic_label("تواصل معنا", 60, {'center_x':0.5,'top':0.90}))

        # Change this to your real form link later
        self.contact_url = "https://forms.gle/YOUR_LINK_HERE"

        layout.add_widget(
            rounded_btn("فتح نموذج التواصل", {'center_x':0.5,'center_y':0.55}, (0.40,0.14), cb=self.open_link)
        )

        layout.add_widget(
            rounded_btn("رجوع", {'center_x':0.5,'y':0.05}, (0.30,0.12), cb=self.go_back)
        )

        self.add_widget(layout)

    def open_link(self, *args):
        webbrowser.open(self.contact_url)

    def go_back(self, *args):
        self.manager.current = "main"

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

