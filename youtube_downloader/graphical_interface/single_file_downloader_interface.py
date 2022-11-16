from base_gui import BaseGui
import util.downlader as downloader


class SingleFileDownloadsGui(BaseGui):
    _interface_elements_x_position = 300

    def __init__(self, parent_frame, main_frame):
        super().__init__(parent_frame, main_frame)
        self._interface_title = 'Youtube Downloader 1.0.5'
        
        #self.title(self._interface_title)

        self._download_path_input_section = self.create_download_path_input_section()
        self._link_input_section = self.create_youtube_link_input_section()
        self._status_display = self.create_status_label()

        self.draw_screen([self._status_display,
                          self._download_path_input_section[0],
                          self._download_path_input_section[1],
                          self._link_input_section[0],
                          self._link_input_section[1],
                          self.create_download_video_button(),
                          self.create_download_mp3_button()])

    def draw_screen(self, interface_elements):
        y_coordinate = 100
        for element in interface_elements:
            self.add_element_to_interface(self._interface_elements_x_position, y_coordinate, element)
            y_coordinate = y_coordinate + 70

    def set_download_path(self):
        downloader.select_download_path(self._download_path_input_section[0])

    def download(self, mediatype):
        self._status_display.config(
            text=f'Starting download for {mediatype}. Please wait...')

        download_status_message = downloader.download_function(
            self._link_input_section[1].get(),
            self._download_path_input_section[0].cget("text"),
            mediatype
        )

        if 'Download failed' in download_status_message:
            self._status_display.config(background='red', width=500, height=5, font=('Kozuka Gothic Pro H', 8))

        self._status_display.config(text=download_status_message)

    def download_video(self):
        self.download('video')

    def download_mp3(self):
        self.download('mp3')

    def create_status_label(self):
        return self.create_label("Download Status: READY")

    def create_youtube_link_input_section(self):
        return self.create_label("Enter download link: "), self.create_text_entry_widget(35)

    def create_download_path_input_section(self):
        return self.create_label("Download directory: ???"), self.create_button("Set directory", self.set_download_path)

    def create_download_video_button(self):
        return self.create_button("Download Video", self.download_video)

    def create_download_mp3_button(self):
        return self.create_button("Download MP3", self.download_mp3)
