# features/quiz_math.py
# Arabic Math Quiz Screen

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from features.ui import arabic_label, rounded_btn, BLUE, YELLOW, RED, BACKGROUND

# Math questions in Arabic
QUESTIONS = [
    {"q": "كم ناتج: 5 + 3 ؟",            "opts":["7","8","9","6"], "ans":"8"},
    {"q": "كم ناتج: 12 - 4 ؟",           "opts":["9","8","7","6"], "ans":"8"},
    {"q": "ما هو العدد بعد 19 ؟",        "opts":["18","19","20","21"], "ans":"20"},
    {"q": "كم يساوي: 2 × 6 ؟",          "opts":["10","11","12","14"], "ans":"12"},
    {"q": "كم يساوي: 15 ÷ 3 ؟",         "opts":["3","4","5","6"], "ans":"5"},
]

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*BACKGROUND)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.index = 0
        self.correct = 0
        self.wrong = 0

        self.show_question()

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def show_question(self):
        self.layout.clear_widgets()

        self.correct_lbl = arabic_label(
            f"إجابات صحيحة: {self.correct}", 34, {'x':0.05,'top':0.95}, color=BLUE
        )
        self.wrong_lbl = arabic_label(
            f"إجابات خاطئة: {self.wrong}", 34, {'right':0.95,'top':0.95}, color=RED
        )

        self.layout.add_widget(self.correct_lbl)
        self.layout.add_widget(self.wrong_lbl)

        if self.index >= len(QUESTIONS):
            return self.show_result()

        q = QUESTIONS[self.index]
        self.layout.add_widget(arabic_label(q['q'], 40, {'center_x':0.5,'top':0.83}))

        ypos = [0.60, 0.47, 0.34, 0.21]
        for i, opt in enumerate(q['opts']):
            btn = rounded_btn(
                opt, {'center_x':0.5, 'center_y':ypos[i]}, (0.45,0.12), BLUE, 32,
                cb=lambda _btn, choice=opt: self.check(choice)
            )
            self.layout.add_widget(btn)

        self.layout.add_widget(rounded_btn(
            "رجوع", {'x':0.05,'y':0.05}, (0.22,0.1), YELLOW, 26,
            cb=lambda *_: setattr(self.manager,'current','main')
        ))
        self.layout.add_widget(rounded_btn(
            "خروج", {'right':0.95,'y':0.05}, (0.22,0.1), RED, 26,
            cb=self.exit_app
        ))

    def check(self, choice):
        if choice == QUESTIONS[self.index]["ans"]:
            self.correct += 1
        else:
            self.wrong += 1

        self.correct_lbl.text = f"إجابات صحيحة: {self.correct}"
        self.wrong_lbl.text = f"إجابات خاطئة: {self.wrong}"

        Clock.schedule_once(lambda dt: self.next_question(), 0.6)

    def next_question(self):
        self.index += 1
        self.show_question()

    def show_result(self):
        self.layout.clear_widgets()

        text = f"نتيجتك:\nإجابات صحيحة: {self.correct}\nإجابات خاطئة: {self.wrong}"
        self.layout.add_widget(arabic_label(
            text, 44, {'center_x':0.5,'center_y':0.62}, width=1000, height=280
        ))

        self.layout.add_widget(rounded_btn(
            "إعادة المحاولة", {'center_x':0.5,'center_y':0.42}, (0.34,0.12), BLUE, 28,
            cb=self.reset_quiz
        ))
        self.layout.add_widget(rounded_btn(
            "رجوع", {'center_x':0.5,'y':0.05}, (0.24,0.1), YELLOW, 26,
            cb=lambda *_: setattr(self.manager,'current','main')
        ))

    def reset_quiz(self, *args):
        self.index = 0
        self.correct = 0
        self.wrong = 0
        self.show_question()

    def exit_app(self, *args):
        from kivy.app import App
        App.get_running_app().stop()
        import sys
        sys.exit()

