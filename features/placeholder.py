# features/placeholder.py

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from features.ui import arabic_label, rounded_btn, BACKGROUND
from kivy.graphics import Color, Rectangle

class PlaceholderScreen(Screen):
    def __init__(self, title_text, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        layout = FloatLayout()

        layout.add_widget(arabic_label(title_text, 56, {'center_x':0.5,'center_y':0.65}))
        layout.add_widget(arabic_label("قيد التطوير", 40, {'center_x':0.5,'center_y':0.50}))

        layout.add_widget(
            rounded_btn("رجوع", {'center_x':0.5,'y':0.05}, (0.30,0.12), cb=self.go_back)
        )

        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = "main"

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

