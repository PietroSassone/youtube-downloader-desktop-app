from tkinter import Canvas, Label, Entry, Button, Frame, GROOVE, CENTER, PhotoImage


class BaseGui(Frame):
    INTERFACE_ELEMENTS_X_POSITION = 300
    BASE_GUI_WIDTH = 600
    BASE_GUI_HEIGHT = 700
    BUTTON_BASE_TEXT_COLOR = 'DarkGoldenrod3'
    FONT = ('Kozuka Gothic Pro H', 20)
    SECONDARY_LABEL_FONT = ('Khmer UI', 10)
    FAILURE_MESSAGE = 'Failure'

    _interface_title = None

    def __init__(self, parent_frame, controller):
        Frame.__init__(self, parent_frame)
        self._controller = controller

        frame = Frame(self, relief=GROOVE)
        frame.pack(fill = 'both', expand = True)

        self._canvas = Canvas(master = frame, width = self.BASE_GUI_WIDTH, height = self.BASE_GUI_HEIGHT)
    
        self._canvas.pack(fill = 'both', expand = True)

        self._background = PhotoImage(file = r'./graphical_interface/images/background.png')

        self._canvas.create_image(
            self.BASE_GUI_WIDTH/2,
            self.BASE_GUI_HEIGHT/2,
            image = self._background,
            anchor = CENTER
        )

    def get_interface_title(self):
        return self._interface_title

    def set_title_to_display(self, title_to_display):
        return self._controller.title(title_to_display)

    def create_text_entry_widget(self, width):
        return Entry(self, width = width, font = self.FONT)

    def create_label(self, label_title, background_color = 'orange', text_color = 'black', font = FONT, height = 1):
        return Label(self, text = label_title, background=background_color, fg = text_color, height = height, font = font)

    def create_button(self, button_title, button_function, button_color = 'maroon', width = 10):
        return Button(
            self,
            text = button_title,
            bg = button_color,
            padx = '20',
            pady = '5',
            font = self.FONT,
            fg = self.BUTTON_BASE_TEXT_COLOR,
            width = width,
            height = 1,
            command = button_function
        )

    def create_button_display_gui_lambda(self, gui_class):
        return lambda: self._controller.display_interface(gui_class)

    def add_element_to_interface(self, x_coordinate, y_coordinate, element):
        self._canvas.create_window(x_coordinate, y_coordinate, window = element)

    def draw_screen(self, start_y_coordinate, increase_coordinate, interface_elements, fixed_x_coordinate = INTERFACE_ELEMENTS_X_POSITION):
        y_coordinate = start_y_coordinate

        for element_to_add in interface_elements:
            self.add_element_to_interface(fixed_x_coordinate, y_coordinate, element_to_add)
            y_coordinate += increase_coordinate

        return y_coordinate
