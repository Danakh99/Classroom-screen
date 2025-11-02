from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

LabelBase.register(name="Arabic", fn_regular="assets/fonts/Tajawal-Regular.ttf")

ASSETS = "assets/science/"

class Draggable(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dragging = True
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if hasattr(self, "dragging") and self.dragging:
            self.center_x = touch.x
            self.center_y = touch.y

    def on_touch_up(self, touch):
        if hasattr(self, "dragging") and self.dragging:
            self.dragging = False
            for zone in self.parent.zones:
                if zone.collide_point(*touch.pos) and zone.zone_type == self.item_type:
                    zone.add_widget(Image(source=self.source, size_hint=(.28, .28)))
                    self.opacity = 0
                    return

class DropZone(FloatLayout):
    def __init__(self, zone_type, **kwargs):
        super().__init__(**kwargs)
        self.zone_type = zone_type

        with self.canvas.before:
            Color(1, 1, 1, .2)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        self.add_widget(Label(
            text=zone_type,
            font_name="Arabic",
            font_size="25sp",
            halign="center",
            valign="middle",
            pos_hint={"center_x": .5, "center_y": .9}
        ))

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class EcosystemScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        layout.add_widget(Image(
            source=f"{ASSETS}backgrounds/forest_bg.png",
            allow_stretch=True, keep_ratio=False, size_hint=(1, 1)
        ))

        layout.add_widget(Label(
            text="🏞️ صَنِّف الكائنات في النظام البيئي",
            font_name="Arabic",
            font_size="35sp",
            pos_hint={"center_x": .5, "center_y": .93}
        ))

        zone_area = BoxLayout(
            pos_hint={"center_x": .5, "center_y": .18},
            size_hint=(.9, .25),
            spacing=25
        )
        layout.add_widget(zone_area)

        zones = [
            DropZone("حيوان", size_hint=(.33, 1)),
            DropZone("نبات", size_hint=(.33, 1)),
            DropZone("غير حي", size_hint=(.33, 1)),
        ]
        for z in zones:
            zone_area.add_widget(z)
        layout.zones = zones

        items = [
            ("animals/bird.png", "حيوان"), ("animals/camel.png", "حيوان"), ("animals/gazelle.png", "حيوان"),
            ("plants/tree.png", "نبات"), ("plants/plant.png", "نبات"),
            ("abiotic/soil.png", "غير حي"), ("abiotic/sun.png", "غير حي"), ("abiotic/rock.png", "غير حي"),
        ]

        x = [.20, .34, .48, .62, .76, .34, .48, .62]
        y = [.65, .65, .65, .65, .65, .52, .52, .52]

        for (src, cls), xx, yy in zip(items, x, y):
            img = Draggable(source=f"{ASSETS}{src}", size_hint=(.11, .11),
                            pos_hint={"center_x": xx, "center_y": yy})
            img.item_type = cls
            layout.add_widget(img)

        back = Button(
            text="رجوع",
            font_name="Arabic",
            size_hint=(.15, .09),
            pos_hint={"x": .02, "y": .02},
            background_color=(.2, .2, .2, .7)
        )
        back.bind(on_release=lambda *a: setattr(self.manager, "current", "science"))
        layout.add_widget(back)
