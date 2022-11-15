from tkinter import Canvas, Label, Entry, Button, Frame, GROOVE, CENTER, PhotoImage


class BaseGui:
    _base_gui_width = 600
    _base_gui_height = 800
    _text_color = 'black'
    _font = ('Kozuka Gothic Pro H', 20)

    def __init__(self, graphical_interface):
        self._graphical_interface = graphical_interface
        self._interface_title = None

        self._frame = Frame(master=self._graphical_interface, relief=GROOVE)
        self._frame.pack(fill='both', expand=True)

        self._canvas = Canvas(master=self._frame, width=self._base_gui_width, height=self._base_gui_height)
    
        self._canvas.pack(fill='both', expand=True)

        self._background = PhotoImage(file=r'../youtube_downloader/graphical_interface/images/background.png')

        self._canvas.create_image(
            self._base_gui_width/2,
            self._base_gui_height/2,
            image=self._background,
            anchor=CENTER
        )

    def get_title(self):
        return self._interface_title

    """     @property
        def get_graphical_interface(self):
            return self._graphical_interface """

    def create_text_entry_widget(self, width):
        return Entry(self._graphical_interface, width=width, font=self._font)

    def create_label(self, label_title, background_color = 'gold'):
        return Label(self._graphical_interface, text=label_title, font=self._font, background=background_color)

    def create_button(self, button_title, button_function, button_color = 'red'):
        return Button(
            self._graphical_interface,
            text=button_title,
            bg=button_color,
            padx='20',
            pady='5',
            font=self._font,
            fg=self._text_color,
            width = 10,
            height= 1,
            command=button_function
        )

    def add_element_to_interface(self, x_coordinate, y_coordinate, element):
        self._canvas.create_window(x_coordinate, y_coordinate, window=element)
