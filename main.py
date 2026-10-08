import arabic_reshaper
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line


def arabic(text):
    return arabic_reshaper.reshape(text)


class IslamicApp(App):
    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        # إطار العنوان
        title_box = BoxLayout(
            size_hint_y=None,
            height=100,
            padding=15
        )

