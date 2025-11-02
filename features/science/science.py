from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase

LabelBase.register(name="Arabic", fn_regular="assets/fonts/Tajawal-Regular.ttf")

class ScienceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        title = Label(
            text="العلوم - اختر نشاطًا",
            font_name="Arabic",
            font_size="35sp",
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2)
        )
        layout.add_widget(title)

        btn_ecosystem = Button(
            text="🌍 النظام البيئي",
            font_name="Arabic",
            font_size="30sp",
            size_hint=(0.9, 0.12),
            pos_hint={"center_x": 0.5}
        )

        def go_ecosystem(instance):
            self.manager.current = "ecosystem"

        btn_ecosystem.bind(on_release=go_ecosystem)
        layout.add_widget(btn_ecosystem)

        # Placeholder activities
        topics = [
            "❓ قريبًا",
            "❓ قريبًا",
            "❓ قريبًا",
            "❓ قريبًا",
            "❓ قريبًا"
        ]
        for t in topics:
            layout.add_widget(Button(
                text=t,
                font_name="Arabic",
                font_size="28sp",
                size_hint=(0.9, 0.12),
                pos_hint={"center_x": 0.5},
                disabled=True
            ))

        back_btn = Button(
            text="رجوع",
            font_name="Arabic",
            font_size="28sp",
            size_hint=(0.2, 0.12),
            pos_hint={"x": 0.02},
            background_color=(1, 0.4, 0.4, 1)
        )

        def go_back(instance):
            self.manager.current = "features"

        back_btn.bind(on_release=go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

