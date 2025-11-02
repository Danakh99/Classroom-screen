# features/science.py
# Arabic Science Placeholder Screen

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from features.ui import arabic_label, rounded_btn, BACKGROUND, BLUE, YELLOW

class ScienceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        # Page title
        layout.add_widget(arabic_label(
            "العلوم",
            60,
            {'center_x':0.5, 'top':0.92}
        ))

        # Coming soon note
        layout.add_widget(arabic_label(
            "سيتم إضافة محتوى العلوم قريباً 🌿🧪🫀",
            42,
            {'center_x':0.5, 'center_y':0.55}
        ))

        # Back button
        layout.add_widget(rounded_btn(
            "رجوع",
            {'center_x':0.5, 'y':0.05},
            (0.32, 0.12),
            YELLOW,
            30,
            cb=lambda *_: setattr(self.manager, 'current', 'main')
        ))

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

