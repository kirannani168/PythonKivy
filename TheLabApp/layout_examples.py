#THIS IS WRITTEN BY RAVIKIRANREDY BALEMLA
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

Builder.load_file("layout_examples.kv")

class ScrollViewExample(ScrollView):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range (0, 100):
            b3 = Button(text=str(i+1), size=(dp(100), dp(100)), size_hint = (None, None))
            self.add_widget(b3)
        """b1 = Button(text="Hello", size = (dp(100),dp(200)), size_hint = (None, None))
        b2 = Button(text="Bye")
        self.add_widget(b1)
        self.add_widget(b2)"""

class GridLayoutExample(GridLayout):
    btn_txt= StringProperty("Initial")
    def change_text(self):
        self.btn_txt = "Final"

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    pass