# features/ui.py
# UI helpers + Arabic text render functions

from kivy.uix.label import Label
from kivy.uix.button import Button
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from kivy.core.text import LabelBase

# --------------------------
# Register Arabic Font
# --------------------------
LabelBase.register(
    name="ArabicFont",
    fn_regular="assets/arabic.ttf"
)

# --------------------------
# Colors
# --------------------------
BACKGROUND = (247/255, 247/255, 247/255, 1)
BLUE       = (15/255, 89/255, 119/255, 1)
YELLOW     = (251/255, 213/255, 14/255, 1)
RED        = (1, 0, 0, 1)
GREEN      = (0, 0.6, 0, 1)
PURPLE     = (0.5, 0, 0.6, 1)
PINK       = (1, 0.6, 0.8, 1)
BLACK      = (0, 0, 0, 1)
WHITE      = (1,1,1,1)

# --------------------------
# Arabic Text Fix
# --------------------------
def bidi_text(text):
    reshaped = reshape(text)
    return get_display(reshaped)

# --------------------------
# Arabic Label
# --------------------------
def arabic_label(text, font_size, pos_hint, color=(0,0,0,1)):
    fixed = bidi_text(text)

    widget = Label(
        text=fixed,
        font_size=font_size,
        font_name="ArabicFont",
        color=color,
        size_hint=(None, None),
        size=(1600, 200),
        pos_hint=pos_hint,
        halign="center",
        valign="middle"
    )
    widget.bind(size=widget.setter('text_size'))
    return widget

# --------------------------
# Arabic Button
# --------------------------
def rounded_btn(text, pos_hint, size_hint=(0.28,0.12), color=BLUE, font_size=30, cb=None):
    fixed = bidi_text(text)

    btn = Button(
        text=fixed,
        font_name="ArabicFont",
        size_hint=size_hint,
        pos_hint=pos_hint,
        background_normal='',
        background_color=color,
        font_size=font_size
    )

    if cb:
        btn.bind(on_release=cb)
    return btn

