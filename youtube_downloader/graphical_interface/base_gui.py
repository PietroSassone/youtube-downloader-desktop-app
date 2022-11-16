from tkinter import Canvas, Label, Entry, Button, Frame, GROOVE, CENTER, PhotoImage


class BaseGui(Frame):
    _base_gui_width = 600
    _base_gui_height = 800
    _text_color = 'black'
    _font = ('Kozuka Gothic Pro H', 20)

    def __init__(self, parent_frame, main_frame):
        Frame.__init__(self, parent_frame)
        self._interface_title = None
        self._controller = main_frame

        self._frame = Frame(self, relief=GROOVE)
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

    def get_frame(self):
        return self._frame

    def create_text_entry_widget(self, width):
        return Entry(self, width=width, font=self._font)

    def create_label(self, label_title, background_color = 'gold'):
        return Label(self, text=label_title, font=self._font, background=background_color)

    def create_button(self, button_title, button_function, button_color = 'red', width = 10):
        return Button(
            self,
            text=button_title,
            bg=button_color,
            padx='20',
            pady='5',
            font=self._font,
            fg=self._text_color,
            width = width,
            height= 1,
            command=button_function
        )

    def add_element_to_interface(self, x_coordinate, y_coordinate, element):
        self._canvas.create_window(x_coordinate, y_coordinate, window=element)
