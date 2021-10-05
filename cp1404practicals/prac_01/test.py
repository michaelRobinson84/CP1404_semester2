from kivy.app import App
from kivy.lang import Builder


class ButtonEventDemo(App):
    def build(self):
        self.title = "Button Event Demo"
        self.root = Builder.load_file("button_event.kv")
        return self.root

    def press_button(self, button):
        print('app: ' + self)
        print(str(button) + " says ouch!")

ButtonEventDemo().run()