import os, sys

def get_image_dir():
    curr_dir = os.getcwd()
    print(curr_dir)
    return os.path.join(curr_dir,"resource/image")

def get_sound_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"resource/sound")

def get_font_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"resource/font")



