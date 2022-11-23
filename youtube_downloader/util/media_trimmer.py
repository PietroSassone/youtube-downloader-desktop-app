import ffmpeg
import file_util


PRESENTATION_TIMESTAMPS = "PTS-STARTPTS"
MP4 = 'mp4'
MP3 = 'mp3'
ALLOWED_MEDIA_TYPES = [MP3, MP4]

@staticmethod
def trim_media(input_file, start_seconds, end_seconds, mediatype):
    if mediatype not in ALLOWED_MEDIA_TYPES:
        raise TypeError(f"Only trimming {ALLOWED_MEDIA_TYPES} extensions is supported. Please check the input file.")

    try:
        trimmed_file_result = f'{input_file}_trimmed_{start_seconds}_{end_seconds}.{mediatype}'
        file_util.delete_file_if_exists(trimmed_file_result)

        input_stream = ffmpeg.input(input_file)
    
        trimmed_file_input = trimmed_audio = (
            input_stream
                .filter_("atrim", start = start_seconds, end = end_seconds)
                .filter_("asetpts", PRESENTATION_TIMESTAMPS)
            )
        
        if MP4 == mediatype:
            trimmed_video = input_stream.trim(start = start_seconds, end = end_seconds).setpts(PRESENTATION_TIMESTAMPS)
            trimmed_file_input = ffmpeg.concat(trimmed_video, trimmed_audio, v = 1, a = 1)
        
        ffmpeg.output(trimmed_file_input, trimmed_file_result, format=mediatype).run()
        
    except Exception as e:
        print(str(e))

    return trimmed_file_result
