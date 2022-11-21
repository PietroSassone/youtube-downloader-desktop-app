# Youtube Media Downloader Desktop App
A lightweight desktop app written in Python to download videos & mp3 files from Youtube.
Written in Python 3.11.0.

**1. Features**
This app has a simple graphical interface.  

It allows the user to:
1. Download full YouTube videos one by one either in mp4 or mp3 format.
1. Download trimmed YouTube videos one by one either in mp4 or mp3 format.
1. Download whole public YouTube playlists at once either in mp4 or mp3 format.

For each download type, the user has to specify the download directory & YouTube URL via the GUI.

*Notes:*
* The download will throw an error message if the YouTube URL is invalid, the download directory has not been set, or the given file already exists.
* The playlist download will only work with public playlist. Also only works with playlist URLs, not with single video URLs.
* When trimming videos, the GUI only accepts integer values as input.  
  - If the trimming start second is bigger than the end second, an error is shown and the input needs to be added again.
  - If the trimming start second is not set, the trimming will start at the very beginning of the media.
  - If the trimming end second is not set, the trimming will end at the very end of the media. The same happens if the trimming end second is set to a bigger value than the actual media length.


**2. Technologies used**
* Python 3.11.0.

Some Python libraries the you will have to install to build & run the code:
* TKinter, for GUI
* MoviePy and PyTube for downloading from YouTube
* FFmpeg and FFmpeg-Python for trimming media


**3. Running the code**
1. Open a terminal in the repo's "youtube_downloader" folder
1. Run the app with ```python application.py```. the GUI should be visible.
