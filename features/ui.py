# features/ui.py

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

# ---------------------------------------
# Colors
# ---------------------------------------
BACKGROUND = (247/255, 247/255, 247/255, 1)
BLUE       = (15/255, 89/255, 119/255, 1)
YELLOW     = (251/255, 213/255, 14/255, 1)
RED        = (1, 0, 0, 1)
GREEN      = (0, 1, 0, 1)
PURPLE     = (0.6, 0, 0.8, 1)
PINK       = (1, 0.6, 0.8, 1)
BLACK      = (0, 0, 0, 1)


# ---------------------------------------
# Arabic Label Helper
# ---------------------------------------
def arabic_label(text, font_size, pos_hint, color=BLUE):
    lab = Label(
        text=text,
        font_size=font_size,
        color=color,
        size_hint=(None, None),
        size=(1600, 140),
        pos_hint=pos_hint,
        halign="center",
        valign="middle"
    )
    lab.bind(size=lab.setter('text_size'))
    return lab


# ---------------------------------------
# Rounded Button Helper
# ---------------------------------------
def rounded_btn(text, pos_hint, size_hint=(0.28,0.1), color=BLUE, font_size=28, cb=None):
    btn = Button(
        text=text,
        size_hint=size_hint,
        pos_hint=pos_hint,
        background_normal='',
        background_color=color,
        font_size=font_size
    )
    if cb:
        btn.bind(on_release=cb)
    return btn


# ---------------------------------------
# Color Circle Button (for notebook)
# ---------------------------------------
def color_dot(color, pos_hint, size=(54,54), cb=None):
    btn = Button(
        background_normal='',
        background_color=color,
        size_hint=(None,None),
        size=size,
        pos_hint=pos_hint
    )
    if cb:
        btn.bind(on_release=cb)
    return btn

