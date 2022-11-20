from base_gui import BaseGui
from trimmed_file_downloader_interface import TrimmedFileDownloaderGui
from playlist_downloader_interface import PlayListDownloaderGui
from single_file_downloader_interface import SingleFileDownloaderGui


class MainMenu(BaseGui):
    BUTTON_WIDTH = 25
    BUTTON_COLOR = 'maroon'
    MENU_LABEL_COLOR = 'DarkOrange4'
    MENU_BUTTONS_Y_COORDINATE_START = 100
    MENU_BUTTONS_Y_COORDINATE_STEPS = 150

    def __init__(self, parent, controller):
        controller.title('Youtube Downloader Main Menu')
        super().__init__(parent, controller) 
    
        self.draw_screen(
            self.MENU_BUTTONS_Y_COORDINATE_START,
            self.MENU_BUTTONS_Y_COORDINATE_STEPS,
            [self.create_label('Main Menu', self.MENU_LABEL_COLOR, self.BUTTON_BASE_TEXT_COLOR),
             self.create_single_file_page_button(),
             self.create_trim_page_button(),
             self.create_playlist_page_button()]
        )
    
    def create_menu_button(self, title, gui_class):
        return self.create_button(title, self.create_button_lambda(gui_class), self.BUTTON_COLOR, self.BUTTON_WIDTH)

    def create_trim_page_button(self):
        return self.create_menu_button('Trimmed single file downloader', TrimmedFileDownloaderGui)

    def create_single_file_page_button(self):
        return self.create_menu_button('Full single file downloader', SingleFileDownloaderGui)

    def create_playlist_page_button(self):
        return self.create_menu_button('Playlist bulk downloader', PlayListDownloaderGui)
