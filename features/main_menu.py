# features/main_menu.py

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

from features.ui import arabic_label, rounded_btn, BACKGROUND, BLUE, YELLOW

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Background
        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        # --- Logo (moved to the left so it's clearly visible) ---
        logo = Image(
            source="assets/Taa.jpg",
            size_hint=(0.22, 0.22),
            pos_hint={"x": 0.03, "top": 0.96},
        )
        layout.add_widget(logo)

        # --- Title (centered) ---
        title = arabic_label(
            "مرحبًا بكم في منصة تاء التعليمية",
            50,
            {"center_x": 0.60, "top": 0.93}
        )
        layout.add_widget(title)

        # --- Buttons (order + spacing + smaller size) ---
        # Requested order:
        # العلوم، الرياضيات، اللغة الإنجليزية، الحاسوب، الاجتماعيات، دفتر الملاحظات، تواصل معنا
        btn_specs = [
            ("العلوم",          "science",  BLUE),
            ("الرياضيات",       "quiz",     BLUE),
            ("اللغة الإنجليزية","english",  BLUE),
            ("الحاسوب",         "computer", BLUE),
            ("الاجتماعيات",     "social",   BLUE),
            ("دفتر الملاحظات",  "notebook", YELLOW),  # yellow per request
            ("تواصل معنا",      "contact",  YELLOW),  # yellow per request
        ]

        # Layout parameters
        btn_width  = 0.42
        btn_height = 0.095
        start_y    = 0.72
        gap        = 0.105  # more space between buttons

        y = start_y
        for text, target, color in btn_specs:
            btn = rounded_btn(
                text,
                {"center_x": 0.60, "center_y": y},
                (btn_width, btn_height),
                color,
                30,
                cb=lambda _, s=target: self._go(s)
            )
            layout.add_widget(btn)
            y -= gap

        # Optional small spacer at bottom
        layout.add_widget(Widget(size_hint=(1, 0.02)))

        # (Exit button kept small & out of the way; remove if not needed)
        exit_btn = rounded_btn(
            "خروج",
            {"center_x": 0.60, "y": 0.015},
            (0.22, 0.075),
            (1, 0, 0, 1),
            26,
            cb=lambda *_: self._exit_app()
        )
        layout.add_widget(exit_btn)

    def _go(self, screen_name: str):
        self.manager.current = screen_name

    def _exit_app(self):
        from kivy.app import App
        import sys
        App.get_running_app().stop()
        sys.exit()

    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

