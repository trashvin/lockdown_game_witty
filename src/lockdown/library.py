from ntpath import join
import os, sys

"""
start : methods for getting the asset file directory
"""
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

def get_files_dir():
    curr_dir = os.getcwd()
    return os.path.join(curr_dir,"assets\\files")

def get_font(font_name):
    return os.path.join(get_font_dir(), font_name)

def get_image(image_name):
    return os.path.join(get_image_dir(), image_name)

def get_sound(sound_name):
    return os.path.join(get_sound_dir(), sound_name)

def get_file(file_name):
    return os.path.join(get_files_dir(), file_name)

"""
start: misc functions
"""
def retrieve_level_layout(level:int):
    file_name = f'level_{level}.lkd'
    elements = []
    try:
        with open(get_file(file_name)) as file:
            for line in file: 
                elements.append(line.split(','))

        return elements
    except:
        return None