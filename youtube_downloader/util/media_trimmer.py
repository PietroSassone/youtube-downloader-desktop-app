import ffmpeg
import file_util


PRESENTATION_TIMESTAMPS = "PTS-STARTPTS"

@staticmethod
def trim_media(input_file, start_seconds, end_seconds, mediatype):
    if mediatype not in ['mp3', 'mp4']:
        raise TypeError("Only trimming mp3 and mp4 is supported. Please check the input file.")

    try:
        trimmed_file_result = f'{input_file}_trimmed_{start_seconds}_{end_seconds}.{mediatype}'
        file_util.delete_file_if_exists(trimmed_file_result)

        input_stream = ffmpeg.input(input_file)
    
        trimmed_file_input = trimmed_audio = (
            input_stream
                .filter_("atrim", start=start_seconds, end=end_seconds)
                .filter_("asetpts", PRESENTATION_TIMESTAMPS)
            )
        
        if 'mp4' == mediatype:
            trimmed_video = input_stream.trim(start=start_seconds, end=end_seconds).setpts(PRESENTATION_TIMESTAMPS)
            trimmed_file_input = ffmpeg.concat(trimmed_video, trimmed_audio, v=1, a=1)
        
        ffmpeg.output(trimmed_file_input, trimmed_file_result, format=mediatype).run()
        
    except Exception as e:
        print(str(e))

    return trimmed_file_result
    