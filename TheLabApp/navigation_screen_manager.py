from kivy.uix.screenmanager import ScreenManager

#THIS IS WRITTEN BY RAVIKIRANREDY BALEMLA
class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        self.screen_stack.append(self.current)
        self.current = screen_name
        self.transition.direction = "left"

    def pop(self):
        screen_name = self.screen_stack[-1]
        del self.screen_stack[-1]
        self.current = screen_name
        self.transition.direction = "right"