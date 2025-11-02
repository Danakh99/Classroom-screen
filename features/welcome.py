# features/welcome.py
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from features.ui import arabic_label, BACKGROUND
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background
        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        # Big centered logo
        layout.add_widget(Image(
            source="assets/Taa.jpg",
            size_hint=(0.55, 0.55),
            pos_hint={"center_x": 0.5, "center_y": 0.63}
        ))

        # Title
        layout.add_widget(arabic_label(
            "مرحبًا بكم في منصة تاء التعليمية",
            55,
            {"center_x": 0.5, "center_y": 0.18}
        ))

        # Auto move to main menu after 2 seconds
        Clock.schedule_once(lambda dt: self.go_next(), 2)

    def go_next(self):
        self.manager.current = "mainmenu"

    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

