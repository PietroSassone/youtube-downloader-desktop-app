from tkinter import Tk
from settings_interface import SettingsInterface
from youtube_downloader_interface import YoutubeDownloaderInterface


class MainFrame:
    def __init__(self):
        self._graphical_interface = Tk()
        self._graphical_interface.resizable(False, False)

        self._downloader_interface = YoutubeDownloaderInterface(self._graphical_interface)
        self._settings_interface = SettingsInterface(self._graphical_interface)
        
        self._downloader_interface.add_element_to_interface(150, 650, self.create_settings_button())
        self._settings_interface.add_element_to_interface(300, 650, self.create_back_to_downloader_button())

    def create_settings_button(self):
        return self._downloader_interface.create_button("Settings", self.go_to_settings, 'silver')

    def create_back_to_downloader_button(self):
        return self._settings_interface.create_button("Downloader", self.go_to_downloader, 'gold')
    
    def go_to_settings(self):
        self._downloader_interface._frame.pack_forget()
        self._settings_interface._frame.pack(fill='both', expand=1)
        self._graphical_interface.title(self._settings_interface.get_title()) 
    
    def go_to_downloader(self):
        self._settings_interface._frame.pack_forget()
        self._downloader_interface._frame.pack(fill='both', expand=1)
        self._graphical_interface.title(self._downloader_interface.get_title())

    def run_app_interface(self):
        self._graphical_interface.mainloop()
