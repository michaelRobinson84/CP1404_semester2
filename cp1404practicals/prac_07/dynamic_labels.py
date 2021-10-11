
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.lst_names = "John, Steve, Emily, Carol, Mathew, Juliet".split(",")

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):

        for name in self.lst_names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()

        # """Create buttons from dictionary entries and add them to the GUI."""
        # for name in self.name_to_phone:
        #     # create a button for each data entry, specifying the text and id
        #     # (although text and id are the same in this case, you should see how this works)
        #     temp_button = Button(text=name)
        #     temp_button.bind(on_release=self.press_entry)
        #     # add the button to the "entries_box" layout widget
        #     self.root.ids.entries_box.add_widget(temp_button)
