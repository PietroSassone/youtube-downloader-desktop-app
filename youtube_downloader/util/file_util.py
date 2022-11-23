import shutil
import os   


@staticmethod
def create_new_mp3_from_file(input_file):
    downloaded_file_name_base = os.path.splitext(input_file)[0]
    new_mp3_file_name = downloaded_file_name_base + '.mp3'
    os.rename(input_file, new_mp3_file_name)

    return new_mp3_file_name

@staticmethod
def move_file(file_name, target_path):
    shutil.move(file_name, target_path)

@staticmethod
def delete_file_if_exists(file):
    if os.path.exists(file):
        os.remove(file)
