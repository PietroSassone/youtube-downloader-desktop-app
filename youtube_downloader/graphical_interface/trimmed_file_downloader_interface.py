from common_file_downloader_interface import DownloaderGuiCommonCore


class TrimmedFileDownloaderGui(DownloaderGuiCommonCore):

    TRIM_SECTION_Y_COORDINATE_START = 350
    TRIM_SECTION_Y_COORDINATE_STEPS = 50
    INPUT_FIELD_WIDTH = 5

    def __init__(self, parent_frame, controller):
        controller.title('Trim & download videos or audios.')
        super().__init__(parent_frame, controller)
        self.add_trim_section()
        self.add_download_section()
    
    def add_trim_section(self):
        self.add_trim_entry_element(self.create_start_label(), 150)
        self.add_trim_entry_element(self.create_end_label(), 450)

    def add_trim_entry_element(self, label, x_coordinate):
        self.draw_screen(
            self.TRIM_SECTION_Y_COORDINATE_START,
            self.TRIM_SECTION_Y_COORDINATE_STEPS,
            [label, self.create_text_entry_widget(self.INPUT_FIELD_WIDTH)],
            x_coordinate
        )

    def add_download_section(self):
        self.draw_screen(
            self._y_coordinate + 100,
            self.Y_COORDINATE_INCREASE_STEPS,
            [self.create_download_video_button(), self.create_download_mp3_button()]
        )

    def create_start_label(self):
        return self.create_label("Start second:"),
    
    def create_end_label(self):
        return self.create_label("End second:"),
            