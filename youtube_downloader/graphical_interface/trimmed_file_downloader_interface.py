from common_file_downloader_interface import DownloaderGuiCommonCore
from tkinter import messagebox, END


class TrimmedFileDownloaderGui(DownloaderGuiCommonCore):

    TRIM_SECTION_Y_COORDINATE_START = 350
    TRIM_SECTION_Y_COORDINATE_STEPS = 50
    INPUT_FIELD_WIDTH = 5
    TRIM_INPUT_UPDATE_EVENT = '<FocusOut>'
    FAILURE_MESSAGE = 'Failure'
    TRIM_INPUT_ERROR_MESSAGE = 'The end of the trimming can\'t be before the start.'

    def __init__(self, parent_frame, controller):
        controller.title('Trim & download videos or audios.')
        super().__init__(parent_frame, controller)
        self._start_seconds_input = self.create_text_entry_widget(self.INPUT_FIELD_WIDTH)
        self._end_seconds_input = self.create_text_entry_widget(self.INPUT_FIELD_WIDTH)

        self.add_trim_section()
        self.add_download_section()

        self._start_seconds_input.bind(self.TRIM_INPUT_UPDATE_EVENT, lambda entry: self.get_start_seconds_input())
        self._end_seconds_input.bind(self.TRIM_INPUT_UPDATE_EVENT, lambda entry: self.get_end_seconds_input())
    
    def add_trim_section(self):
        self.add_trim_entry_element(self.create_start_label(), self._start_seconds_input, 150)
        self.add_trim_entry_element(self.create_end_label(), self._end_seconds_input, 450)

    def add_trim_entry_element(self, label, entry, x_coordinate):
        self.draw_screen(
            self.TRIM_SECTION_Y_COORDINATE_START,
            self.TRIM_SECTION_Y_COORDINATE_STEPS,
            [label, entry],
            x_coordinate
        )

    def add_download_section(self):
        self.draw_screen(
            self._y_coordinate + 100,
            self.Y_COORDINATE_INCREASE_STEPS,
            [self.create_download_video_button(), self.create_download_mp3_button()]
        )

    def create_start_label(self):
        return self.create_label('Start second:'),
    
    def create_end_label(self):
        return self.create_label('End second:'),

    def validate_input_is_integer(self, input_field):
        input = input_field.get()
        if not input.isnumeric():
            messagebox.showinfo(self.FAILURE_MESSAGE, 'Please provide an integer number that is at least 0.')
            input = None
            input_field.delete(0, END)
        return input

    def comparison_error_popup(self):
        messagebox.showinfo(self.FAILURE_MESSAGE, self.TRIM_INPUT_ERROR_MESSAGE)

    def get_start_seconds_input(self):
        start_seconds_input = self.validate_input_is_integer(self._start_seconds_input)
        end_seconds_input = self._trim_end_seconds
        
        if end_seconds_input is not None and start_seconds_input > end_seconds_input:
            self.comparison_error_popup()
            start_seconds_input = None
            self._start_seconds_input.delete(0, END)

        self._trim_start_seconds = start_seconds_input

    def get_end_seconds_input(self):
        end_seconds_input = self.validate_input_is_integer(self._end_seconds_input)
        start_seconds_input = self._trim_start_seconds

        if start_seconds_input is not None and start_seconds_input > end_seconds_input:
            self.comparison_error_popup()
            end_seconds_input = None
            self._end_seconds_input.delete(0, END)

        self._trim_end_seconds = end_seconds_input


