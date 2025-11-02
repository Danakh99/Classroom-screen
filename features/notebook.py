# features/notebook.py
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.widget import Widget
from features.ui import rounded_btn, color_dot, BLUE, YELLOW, RED, GREEN, PURPLE, PINK, BLACK, BACKGROUND

class NotebookCanvas(Widget):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.pen_color = BLUE
        self.pen_width = 6
        self.eraser_on = False
        self.eraser_width = 18
        self.line_spacing = 60
        self._active_touches = set()

        self.bind(size=self._redraw_layers, pos=self._redraw_layers)
        self._redraw_layers()

    def _redraw_layers(self, *_):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*BACKGROUND)
            Rectangle(size=self.size, pos=self.pos)

        self.canvas.after.clear()
        with self.canvas.after:
            Color(0.85, 0.85, 0.85, 1)
            y = 0
            while y < self.height:
                Line(points=[0, y, self.width, y], width=1)
                y += self.line_spacing

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return super().on_touch_down(touch)

        self._active_touches.add(touch)
        if getattr(touch, "is_mouse_scrolling", False) or len(self._active_touches) > 1:
            return super().on_touch_down(touch)

        width = self.eraser_width if self.eraser_on else self.pen_width
        with self.canvas:
            Color(*BACKGROUND if self.eraser_on else self.pen_color)
            touch.ud["line"] = Line(points=[touch.x, touch.y], width=width)
        return True

    def on_touch_move(self, touch):
        if touch not in self._active_touches or len(self._active_touches) > 1:
            return super().on_touch_move(touch)

        if "line" in touch.ud:
            touch.ud["line"].points += [touch.x, touch.y]
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch in self._active_touches:
            self._active_touches.remove(touch)
        return super().on_touch_up(touch)

class NotebookScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = FloatLayout()
        self.add_widget(layout)

        self.scroll = ScrollView(
            size_hint=(1, 0.88), pos_hint={'x': 0, 'y': 0.12},
            do_scroll_x=False, do_scroll_y=True,
            scroll_type=['bars', 'content'],
            bar_width=16,
            bar_color=(0, 0, 0, 1),
            bar_inactive_color=(0, 0, 0, 0.35),
        )

        self.canvas_area = NotebookCanvas(size_hint_y=None, height=2600)
        self.scroll.add_widget(self.canvas_area)
        layout.add_widget(self.scroll)

        layout.add_widget(Label(text="حجم القلم", font_size=18, color=BLUE,
            size_hint=(None,None), size=(80,60), pos_hint={'x':0.005,'center_y':0.86}))
        self.pen_slider = Slider(min=1,max=24,value=self.canvas_area.pen_width,
            orientation='vertical', size_hint=(None,0.46), width=56,
            pos_hint={'x':0.01,'center_y':0.68})
        self.pen_slider.bind(value=self.change_pen_size)
        layout.add_widget(self.pen_slider)

        layout.add_widget(Label(text="حجم الممحاة", font_size=18, color=BLUE,
            size_hint=(None,None), size=(80,60), pos_hint={'x':0.005,'center_y':0.44}))
        self.eraser_slider = Slider(min=6,max=40,value=self.canvas_area.eraser_width,
            orientation='vertical', size_hint=(None,0.46), width=56,
            pos_hint={'x':0.01,'center_y':0.26})
        self.eraser_slider.bind(value=self.change_eraser_size)
        layout.add_widget(self.eraser_slider)

        colors = [BLUE, YELLOW, RED, GREEN, PURPLE, PINK, BLACK]
        start_x = 0.30
        step = 0.06
        for i, c in enumerate(colors):
            layout.add_widget(color_dot(
                c, pos_hint={'center_x':start_x+i*step,'y':0.02},
                cb=lambda _btn, col=c: self.set_color(col)))

        self.eraser_btn = rounded_btn(
            "الممحاة: مغلقة", {'right':0.97,'y':0.01},
            (0.16,0.08), YELLOW, 22, cb=self.toggle_eraser)
        layout.add_widget(self.eraser_btn)

        layout.add_widget(rounded_btn(
            "مسح الصفحة", {'x':0.08,'y':0.01},
            (0.12,0.08), YELLOW, 22, cb=self.clear_canvas))

        # ✅ FIX BACK BUTTON—GO BACK TO MAINMENU
        layout.add_widget(rounded_btn(
            "رجوع", {'right':0.97,'top':0.98},
            (0.14,0.08), YELLOW, 24,
            cb=lambda *_: setattr(self.manager, "current", "mainmenu")
        ))

    def _update_bg(self, *_):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def change_pen_size(self, _slider, value):
        self.canvas_area.pen_width = value

    def change_eraser_size(self, _slider, value):
        self.canvas_area.eraser_width = value

    def set_color(self, color):
        self.canvas_area.pen_color = color
        self.canvas_area.eraser_on = False
        self.eraser_btn.text = "الممحاة: مغلقة"

    def toggle_eraser(self, *_):
        self.canvas_area.eraser_on = not self.canvas_area.eraser_on
        self.eraser_btn.text = "الممحاة: مفتوحة" if self.canvas_area.eraser_on else "الممحاة: مغلقة"

    def clear_canvas(self, *_):
        self.canvas_area.canvas.clear()
        self.canvas_area._redraw_layers()

