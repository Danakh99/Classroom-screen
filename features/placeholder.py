# features/placeholder.py

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from features.ui import BACKGROUND, arabic_label, rounded_btn, BLUE, YELLOW

class PlaceholderScreen(Screen):
    def __init__(self, title_text="قريباً", **kw):
        super().__init__(**kw)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        layout.add_widget(arabic_label(
            title_text,
            48,
            {'center_x': 0.5, 'center_y': 0.6},
            color=BLUE
        ))

        layout.add_widget(rounded_btn(
            "رجوع",
            pos_hint={'center_x': 0.5, 'y': 0.05},
            size_hint=(0.2, 0.1),
            color=YELLOW,
            font_size=28,
            cb=lambda *_: setattr(self.manager, "current", "mainmenu")
        ))

    def _update_bg(self, *_):
        self.bg.size = self.size
        self.bg.pos = self.pos

