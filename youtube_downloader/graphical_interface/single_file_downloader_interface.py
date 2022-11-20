from common_file_downloader_interface import DownloaderGuiCommonCore


class SingleFileDownloaderGui(DownloaderGuiCommonCore):

    def __init__(self, parent_frame, controller):
        super().__init__(parent_frame, controller)
        controller.title('Download single media files.')
        self.add_download_buttons()

    def add_download_buttons(self):
        self.draw_screen(
            self._y_coordinate,
            self.Y_COORDINATE_INCREASE_STEPS,
            [self.create_download_video_button(), self.create_download_mp3_button()]
        )
        
        