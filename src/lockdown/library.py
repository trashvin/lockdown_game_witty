import os, sys

def get_image_dir():
    curr_dir = os.getcwd()
    print(curr_dir)
    return os.path.join(curr_dir,"assets\\images")

def get_sound_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"assets\\sounds")

def get_font_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"assets\\fonts")

def get_font(font_name):
    return os.path.join(get_font_dir(), font_name)

def get_image(image_name):
    return os.path.join(get_image_dir(), image_name)




