from tkinter import Tk, Frame
from trimmed_file_downloader_interface import TrimmedFileDownloaderGui
from playlist_downloader_interface import PlayListDownloaderGui
from single_file_downloader_interface import SingleFileDownloaderGui
from main_menu import MainMenu
from PIL import Image, ImageTk


class MainFrame(Tk):
    MENU_BUTTON_Y_COORDINATE = 630

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.wm_iconphoto(False, ImageTk.PhotoImage(Image.open(r'./graphical_interface/images/logo.png')))

        main_frame = Frame(self)
        main_frame.pack(side = "top", fill = "both", expand = False)
        self.resizable(False, False)

        self.interface_frames = self.initialize_all_frames(main_frame)

        self.display_interface(MainMenu)

    def initialize_all_frames(self, main_frame):
        all_frames = {}
        for interface_class in (MainMenu, SingleFileDownloaderGui, TrimmedFileDownloaderGui, PlayListDownloaderGui):
            
            interface_frame = interface_class(main_frame, self)

            self.add_back_to_menu_button(interface_class, interface_frame)

            all_frames[interface_class] = interface_frame

            interface_frame.grid(row = 0, column = 0)
        return all_frames

    def add_back_to_menu_button(self, interface_class, interface_frame):
        if interface_class is not MainMenu:
            interface_frame.add_element_to_interface(
                interface_class.INTERFACE_ELEMENTS_X_POSITION, 
                self.MENU_BUTTON_Y_COORDINATE, 
                self.create_back_to_main_menu_button(interface_frame)
            )

    def display_interface(self, interface_class):
        interface_to_display = self.interface_frames[interface_class]
        interface_to_display.set_title_to_display(interface_to_display.get_interface_title())
        interface_to_display.tkraise()

    @staticmethod
    def create_back_to_main_menu_button(interface):
        return interface.create_button('Back to menu', interface.create_button_display_gui_lambda(MainMenu), MainMenu.MENU_LABEL_COLOR)

    def run_app_interface(self):
        self.mainloop()
