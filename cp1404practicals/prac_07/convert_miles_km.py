from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Michael Robinson'

MILES_TO_KILOMETRES = 1.61


class ConvertMilesToKm(App):

    output_text = StringProperty()

    def build(self):

        Window.size = (500, 250)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, amount):

        current_num = self.convert_to_number(self.root.ids.input_miles.text)

        current_num += amount
        self.root.ids.input_miles.text = str(current_num)

    def handle_calculate(self):

        num_in_miles = self.convert_to_number(self.root.ids.input_miles.text)
        num_in_km = num_in_miles * MILES_TO_KILOMETRES
        self.output_text = str(num_in_km)

    def convert_to_number(self, text_to_convert):

        try:
            converted_number = float(text_to_convert)
            return converted_number
        except ValueError:
            return 0.0


ConvertMilesToKm().run()