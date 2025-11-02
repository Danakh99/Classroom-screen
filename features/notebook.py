# features/notebook.py
# Arabic Notebook / Drawing Screen

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Line
from features.ui import arabic_label, rounded_btn, BLUE, YELLOW, BACKGROUND

class DrawingCanvas(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Background
        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        self.pen_color = BLUE
        self.pen_width = 6
        self.current_line = None

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        with self.canvas:
            Color(*self.pen_color)
            self.current_line = Line(points=[touch.x, touch.y], width=self.pen_width)
        return True

    def on_touch_move(self, touch):
        if self.current_line:
            self.current_line.points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()
        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)


class NotebookScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Screen background
        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        layout = FloatLayout()
        self.draw_area = DrawingCanvas(size_hint=(1,0.88), pos_hint={'x':0,'y':0.12})
        layout.add_widget(self.draw_area)

        # Clear button
        layout.add_widget(rounded_btn(
            "مسح",
            {"x":0.05, "y":0.02},
            (0.2, 0.10),
            YELLOW,
            26,
            cb=lambda *_: self.draw_area.clear_canvas()
        ))

        # Back button
        layout.add_widget(rounded_btn(
            "رجوع",
            {"right":0.95, "y":0.02},
            (0.2, 0.10),
            YELLOW,
            26,
            cb=lambda *_: setattr(self.manager, "current", "main")
        ))

        # Colors row (close together)
        colors = [
            BLUE,
            (1,0,0,1),     # Red
            (0,1,0,1),     # Green
            (0.6,0,0.8,1), # Purple
            (1,0.6,0.8,1), # Pink
            (251/255, 213/255, 14/255, 1), # Yellow
        ]

        x_start = 0.28
        for i, c in enumerate(colors):
            btn = rounded_btn("", {"center_x": x_start + i*0.06, "y":0.02}, (None,None), c, 1)
            btn.size_hint = (None,None)
            btn.size = (50,50)
            btn.bind(on_release=lambda _btn, col=c: self.set_pen_color(col))
            layout.add_widget(btn)

        self.add_widget(layout)

    def set_pen_color(self, color):
        self.draw_area.pen_color = color

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

