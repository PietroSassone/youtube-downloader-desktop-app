from common_file_downloader_interface import DownloaderGuiCommonCore
import util.downlader as downloader


class PlayListDownloaderGui(DownloaderGuiCommonCore):
    BUTTON_WIDTH = 25
    BUTTON_COLOR = 'maroon'

    def __init__(self, parent_frame, controller):
        super().__init__(parent_frame, controller)
        controller.title('Download multiple videos/audios at once from playlists.')
        self.add_download_buttons()

    def add_download_buttons(self):
        self.draw_screen(
            self._y_coordinate,
            self.Y_COORDINATE_INCREASE_STEPS,
            [self.create_download_playlist_videos_button(), 
            self.create_download_playlist_mp3_button(),
            self.create_warning_label()]
        )

    def download_playlist(self, mediatype):
        self._status_display.config(text=f'Starting playlist download for {mediatype}. Please wait...')

        download_status_message = downloader.download_playlist(
            self._link_input_section[1].get(),
            self._download_path_input_section[0].cget("text"),
            mediatype
        )

        if 'Download failed' in download_status_message:
            self._status_display.config(background='red', width=500, height=5, font=('Kozuka Gothic Pro H', 8))

        self._status_display.config(text=download_status_message)

    def download_playlist_videos(self):
        self.download_playlist(self.VIDEO_MEDIA_TYPE)
    
    def download_playlist_audios(self):
        self.download_playlist(self.MP3_MEDIA_TYPE)

    def create_menu_button(self, title, command):
        return self.create_button(title, command, self.BUTTON_COLOR, self.BUTTON_WIDTH)

    def create_download_playlist_videos_button(self):
        return self.create_menu_button('Download playlist as videos', self.download_playlist_videos)

    def create_download_playlist_mp3_button(self):
        return self.create_menu_button('Download playlist as mp3', self.download_playlist_audios)

    def create_warning_label(self):
        return self.create_label('Warning: please provide a playlist link.\nIt won\'t work with single video.\nOnly works for public YouTube playlists!', 'red')

