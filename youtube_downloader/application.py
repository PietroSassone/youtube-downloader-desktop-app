from graphical_interface.youtube_downloader_interface import *
from graphical_interface.main_frame import *

class Application:
    def main():
        """  graphic_user_interface = YoutubeDownloaderInterface()
            graphic_user_interface.run_app_interface() """
            
        MainFrame().run_app_interface()

    if __name__ == "__main__":
        main()
