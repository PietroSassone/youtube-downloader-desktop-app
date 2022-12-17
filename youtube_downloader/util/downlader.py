from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube, Playlist
import subprocess
import file_util
import media_trimmer as media_trimmer


SUCCESS_MESSAGE = 'Download complete.\nStart another download or close the program.'
FAILURE_MESSAGE = '''Download failed. Please try again.\nMaybe the file already exists?
                    \nAlso sake sure the you\'ve provided a valid download link & download path.'''

@staticmethod
def download_single_file(youtube_link, download_path, mediatype, trim_start, trim_end):
    download_status_message = SUCCESS_MESSAGE
    try:
        match mediatype:
            case 'video':
                mp4_video = YouTube(youtube_link).streams.get_highest_resolution().download(download_path)
                   
                result_mp4_file = trim_if_needed(trim_start, trim_end, mp4_video, media_trimmer.MP4)
                
                VideoFileClip(result_mp4_file).close()
        
            case 'mp3':
                downloaded_file = YouTube(youtube_link).streams.filter(only_audio = True).first().download()
                
                result_mp3_file = trim_if_needed(
                                    trim_start, 
                                    trim_end, 
                                    file_util.create_new_mp3_from_file(downloaded_file), 
                                    media_trimmer.MP3
                                  )

                file_util.move_file(result_mp3_file, download_path)
            case _:
                download_status_message = 'Unsupported media type. Please choose video or MP3 format.'

    except Exception as e:
        download_status_message = FAILURE_MESSAGE
        print(str(e))

    return download_status_message

@staticmethod
def trim_if_needed(trim_start, trim_end, input_file, mediatype):
    result_file = input_file

    if not trim_start:
        trim_start = 0

    if not trim_end:
        media_length = get_media_length(input_file)
        trim_end = media_length

    if int(trim_start) > 0 or trim_end is not media_length:
        print(f'Trimming media from {trim_start} to {trim_end} seconds.')
        result_file = media_trimmer.trim_media(input_file, trim_start, trim_end, mediatype)
        file_util.delete_file_if_exists(input_file)
    return result_file

@staticmethod
def get_media_length(input_file):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", input_file],
                              stdout = subprocess.PIPE,
                              stderr = subprocess.STDOUT)
    return float(result.stdout)

@staticmethod
def download_playlist(youtube_link, download_path, mediatype):
    download_status_message = None

    try:
        for video_url in Playlist(youtube_link).video_urls:
            download_status_message = download_single_file(video_url, download_path, mediatype, None, None)

    except Exception as e:
        download_status_message = FAILURE_MESSAGE
        print(str(e))

    return download_status_message
