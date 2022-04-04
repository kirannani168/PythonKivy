#THIS IS WRITTEN BY RAVIKIRANREDY BALEMLA
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_exapmles.kv")

class ImageExample(GridLayout):
    pass

class WidgetsExample(GridLayout):
    count_enabled = BooleanProperty(False)
    toggle_state_text = StringProperty("OFF")
    txt = StringProperty("Helloo")
    count = 0
    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.txt = str(self.count)
    def showing_state(self,widget):
        print("State: ", widget.state)
        if (widget.state == "normal"):
            self.toggle_state_text = "OFF"
            self.count_enabled = False

        else:
            self.toggle_state_text = "ON"
            self.count_enabled = True
    def on_swicth_active(self,widget):
        print("Swicth: ", str(widget.active))