from base_gui import BaseGui
from single_file_downloader_interface import SingleFileDownloadsGui
from trimmed_file_downloader_interface import TrimmedFileDownloadsGui 

class MainMenu(BaseGui):
    def __init__(self, parent, controller):
        super().__init__(parent, controller) 
        #self.title('Main Menu')
  
        self.add_element_to_interface(300, 150, self.create_label('Main Menu'))
        self.add_element_to_interface(300, 300, self.create_single_file_page_button())
        self.add_element_to_interface(300, 450, self.create_trim_page_button())

    def create_trim_page_button(self):
        return self.create_button('Trimmed file downloader', lambda: self._controller.display_interface(TrimmedFileDownloadsGui), 'red', 20)

    def create_single_file_page_button(self):
        return self.create_button('Single file downloader', lambda: self._controller.display_interface(SingleFileDownloadsGui), 'red', 20)
