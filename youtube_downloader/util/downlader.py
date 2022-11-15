from moviepy.editor import VideoFileClip
from pytube import YouTube
from tkinter import filedialog
import file_util
import media_trimmer as media_trimmer


@staticmethod
def select_download_path(path_selector_label):
    path_selector_label.config(text=filedialog.askdirectory())

@staticmethod
def download_function(youtube_link, download_path, mediatype):
    download_status_message = None
    try:
        match mediatype:
            case 'video':
                mp4_video = YouTube(youtube_link).streams.get_highest_resolution().download(download_path)

                mp4_video = media_trimmer.trim_media(mp4_video, 10, 15, "mp4")
                
                VideoFileClip(mp4_video).close()
        
            case 'mp3':
                downloaded_file = YouTube(youtube_link).streams.filter(only_audio=True).first().download()

                new_mp3_file = file_util.create_new_mp3_from_file(downloaded_file)

                new_mp3_file = media_trimmer.trim_media(new_mp3_file, 10, 15, "mp3")

                file_util.move_file(new_mp3_file, download_path)
            case _:
                download_status_message = 'Unsopported media type. Please choose video or MP3 format.'

        download_status_message = 'Download complete.\nStart another download or close the program.'
    except Exception as e:
        download_status_message = '''Download failed. Please try again.\nMaybe the file already exists?
                                    \nAlso sake sure the you\'ve provided a valid download link.'''
        print(str(e))

    return download_status_message
