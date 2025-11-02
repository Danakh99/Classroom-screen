# features/ui.py

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase

import arabic_reshaper
from bidi.algorithm import get_display

# ✅ Register Arabic font
LabelBase.register(name="ArabicFont", fn_regular="assets/arabic.ttf")

# ---------- Colors ----------
BACKGROUND = (247/255, 247/255, 247/255, 1)
BLUE = (15/255, 89/255, 119/255, 1)
YELLOW = (251/255, 213/255, 14/255, 1)
RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
PURPLE = (0.6, 0, 0.8, 1)
PINK = (1, 0.6, 0.8, 1)
BLACK = (0, 0, 0, 1)


# ✅ Fix Arabic (reshape + bidi)
def fix_arabic(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


# ---------- Label helper ----------
def arabic_label(text, font_size, pos_hint, color=BLUE):
    text = fix_arabic(text)
    lab = Label(
        text=text,
        font_size=font_size,
        color=color,
        font_name="ArabicFont",
        halign="center",
        valign="middle",
        size_hint=(None, None),
        size=(1800, 200),
        pos_hint=pos_hint
    )
    lab.bind(size=lab.setter('text_size'))
    return lab


# ---------- Button helper ----------
def rounded_btn(text, pos_hint, size_hint=(0.25, 0.115), color=BLUE, font_size=32, cb=None):
    text = fix_arabic(text)
    btn = Button(
        text=text,
        size_hint=size_hint,
        pos_hint=pos_hint,
        background_normal='',
        background_color=color,
        font_size=font_size,
        font_name="ArabicFont"
    )
    if cb:
        btn.bind(on_release=cb)
    return btn


# ---------- Color button (for notebook) ----------
def color_dot(color, pos_hint, size=(50, 50), cb=None):
    btn = Button(
        background_normal='',
        background_color=color,
        size_hint=(None, None),
        size=size,
        pos_hint=pos_hint
    )
    if cb:
        btn.bind(on_release=cb)
    return btn

