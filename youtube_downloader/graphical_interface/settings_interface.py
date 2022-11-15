from base_gui import BaseGui

class SettingsInterface(BaseGui):
    def __init__(self, graphical_interface):
        super().__init__(graphical_interface)
        self._interface_title = 'Settings'
        self.add_element_to_interface(300, 300, self.create_explanation_label())
        self.add_element_to_interface(150, 400, self.create_start_label())
        self.add_element_to_interface(450, 400, self.create_end_label())
        self.add_element_to_interface(150, 450, self.create_text_entry_widget(5))
        self.add_element_to_interface(450, 450, self.create_text_entry_widget(5))
    
    def create_explanation_label(self):
        return self.create_label("Here you can set the start and end seconds\nfor trimming the downloaded file."),

    def create_start_label(self):
        return self.create_label("Start second:"),
    
    def create_end_label(self):
        return self.create_label("End second:"),
    