from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from features.ui import BACKGROUND, rounded_btn, arabic_label, BLUE, YELLOW, RED


# -------------------------------
# Welcome Screen
# -------------------------------
class WelcomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        layout.add_widget(Image(
            source="assets/Taa.jpg",
            size_hint=(0.45, 0.45),
            pos_hint={'center_x': 0.5, 'center_y': 0.65},
            allow_stretch=True
        ))

        layout.add_widget(arabic_label(
            "مرحبًا بكم في منصة تاء التعليمية",
            52,
            {'center_x': 0.5, 'center_y': 0.35},
            color=BLUE
        ))

        layout.add_widget(rounded_btn(
            "ابدأ",
            pos_hint={'center_x': 0.65, 'y': 0.05},
            size_hint=(0.22, 0.1),
            color=YELLOW,
            font_size=32,
            cb=lambda *_: setattr(self.manager, "current", "mainmenu")
        ))

        layout.add_widget(rounded_btn(
            "خروج",
            pos_hint={'center_x': 0.35, 'y': 0.05},
            size_hint=(0.22, 0.1),
            color=RED,
            font_size=32,
            cb=lambda *_: self.exit_app()
        ))

    def _update_bg(self, *_):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def exit_app(self):
        import sys
        from kivy.app import App
        App.get_running_app().stop()
        sys.exit()


# -------------------------------
# Main Menu Screen
# -------------------------------
class MainMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        layout.add_widget(Image(
            source="assets/Taa.jpg",
            size_hint=(0.18, 0.18),
            pos_hint={'x': 0.02, 'top': 1}
        ))

        layout.add_widget(arabic_label(
            "اختر المادة",
            42,
            {'center_x': 0.5, 'top': 0.95},
            color=BLUE
        ))

        buttons = [
            ("العلوم", "science"),
            ("الرياضيات", "quiz"),
            ("اللغة الإنجليزية", "english"),
            ("الحاسوب", "computer"),
            ("الاجتماعيات", "social"),
            ("دفتر الملاحظات", "notebook"),
            ("تواصل معنا", "contact")
        ]

        y = 0.75
        for text, screen in buttons:
            layout.add_widget(rounded_btn(
                text,
                pos_hint={'center_x': 0.5, 'center_y': y},
                size_hint=(0.35, 0.09),
                color=YELLOW if text in ("دفتر الملاحظات", "تواصل معنا") else BLUE,
                font_size=30,
                cb=lambda _btn, s=screen: setattr(self.manager, "current", s)
            ))
            y -= 0.11

        layout.add_widget(rounded_btn(
            "رجوع",
            pos_hint={'x': 0.02, 'y': 0.02},
            size_hint=(0.18, 0.09),
            color=YELLOW,
            font_size=28,
            cb=lambda *_: setattr(self.manager, "current", "welcome")
        ))

    def _update_bg(self, *_):
        self.bg.size = self.size
        self.bg.pos = self.pos

