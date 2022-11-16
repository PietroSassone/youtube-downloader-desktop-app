from tkinter import Tk, Frame
from trimmed_file_downloader_interface import TrimmedFileDownloadsGui
from single_file_downloader_interface import SingleFileDownloadsGui
from playlist_downloader_interface import PlayListDownloaderGui
from main_menu import MainMenu


class MainFrame(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        main_frame = Frame(self)
        main_frame.pack(side="top", fill="both", expand=False)
        self.resizable(False, False)

        self.interface_frames = {}

        for interface_class in (MainMenu, SingleFileDownloadsGui, TrimmedFileDownloadsGui, PlayListDownloaderGui):

            interface_frame = interface_class(main_frame, self)

            self.interface_frames[interface_class] = interface_frame

            interface_frame.grid(row=0, column=0)

        self.display_interface(MainMenu)

    def display_interface(self, interface_class):
        self.interface_frames[interface_class].tkraise()

    def run_app_interface(self):
        self.mainloop()
