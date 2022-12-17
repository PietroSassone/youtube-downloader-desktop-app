from base_gui import BaseGui
from tkinter import filedialog, messagebox
import util.downlader as downloader


class DownloaderGuiCommonCore(BaseGui):
    Y_COORDINATE_START = 30
    Y_COORDINATE_INCREASE_STEPS = 70
    VIDEO_MEDIA_TYPE = 'video'
    MP3_MEDIA_TYPE = 'mp3'
    SET_DOWNLOAD_PATH_MESSAGE = 'Download directory: PLEASE CHOOSE!'

    _trim_start_seconds = None
    _trim_end_seconds = None

    def __init__(self, parent_frame, main_frame):
        super().__init__(parent_frame, main_frame)

        self._download_path_input_section = self.create_download_path_input_section()
        self._link_input_section = self.create_youtube_link_input_section()
        self._status_display = self.create_status_label()

        self._y_coordinate = self.draw_screen(
                                self.Y_COORDINATE_START,
                                self.Y_COORDINATE_INCREASE_STEPS,
                                [self._status_display,
                                self._download_path_input_section[0],
                                self._download_path_input_section[1],
                                self._link_input_section[0],
                                self._link_input_section[1]]
                            )

    def set_download_path(self):
        self._download_path_input_section[0].config(text = filedialog.askdirectory())

    def download_single_file(self, mediatype):
        download_path = self._download_path_input_section[0].cget('text')
        if self.SET_DOWNLOAD_PATH_MESSAGE == download_path:
            messagebox.showinfo(self.FAILURE_MESSAGE, 'Please set a download directory!')

        else:
            self.set_download_result_message_style('orange')

            self.change_status_message(
                downloader.download_single_file(
                    self._link_input_section[1].get(),
                    download_path,
                    mediatype,
                    self._trim_start_seconds,
                    self._trim_end_seconds
                )
            )      

    def set_download_result_message_style(self, label_color):
        self._status_display.config(background = label_color, width = 200, height = 5, font = self.SECONDARY_LABEL_FONT)

    def change_status_message(self, status_message):
        if 'Download failed' in status_message:
            self.set_download_result_message_style('red')
        self._status_display.config(text = status_message)

    def download_video(self):
        self.download_single_file(self.VIDEO_MEDIA_TYPE)

    def download_mp3(self):
        self.download_single_file(self.MP3_MEDIA_TYPE)

    def create_status_label(self):
        return self.create_label('Download Status: READY')

    def create_youtube_link_input_section(self):
        return self.create_label('Enter download link: '), self.create_text_entry_widget(35)

    def create_download_path_input_section(self):
        return self.create_label(self.SET_DOWNLOAD_PATH_MESSAGE), self.create_button('Set directory', self.set_download_path, 'red')

    def create_download_video_button(self):
        return self.create_button('Download Video', self.download_video)

    def create_download_mp3_button(self):
        return self.create_button('Download MP3', self.download_mp3)
