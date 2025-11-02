# features/science.py
# Arabic Science Placeholder Screen

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from features.ui import arabic_label, rounded_btn, BACKGROUND, YELLOW

class ScienceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        layout.add_widget(arabic_label("العلوم", 56, {'center_x':0.5,'top':0.90}))
        layout.add_widget(arabic_label("سيتم إضافة محتوى العلوم قريباً", 44, {'center_x':0.5,'center_y':0.55}))

        # Back bottom-left
        layout.add_widget(rounded_btn(
            "رجوع", {'x':0.05,'y':0.03}, (0.22,0.09), YELLOW, 28,
            cb=lambda *_: setattr(self.manager,'current','mainmenu')
        ))

    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

