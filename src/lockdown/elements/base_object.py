import os,sys
import pygame as pg
from pygame.locals import *
from lockdown.library import get_image_dir, get_sound_dir


class BaseObject:

    def __init__(self,screen,size, logger, name = "Base Object"):
        self.__screen = screen
        self.__position = (0,0)
        self.__size = size
        self.__name = name
        self.__image = None
        self.__sound = None
        self.__rect = None
        self.__images = []
        self.__log = logger

    def __get_image(self, file_name, image_type = 0):
        # image_type 0 : regular ; 1 : with transparency
        
        img_file = os.path.join(get_image_dir(), file_name)

        if image_type == 0:
            image = pg.image.load(img_file).convert()
        else:
            image = pg.image.load(img_file)

        return image

    def set_image(self,file_name,image_type = 0):
        image = self.__get_image(file_name, image_type)
        self.__image =pg.transform.scale(image,self.__size)
        self.__image.set_colorkey([250,250,0],RLEACCEL)
        self.__rect = self.image.get_rect()

    # def set_images(self, list_of_filenames, image_type = 0):
    #     for file in list_of_filenames:
    #         image = self.__get_image(file, image_type)
    #         image = pg.transform.scale(image,self.__size)
    #         self.__image.set_colorkey([250,250,0],RLEACCEL)
    #         self.__rect = self.image.get_rect()
    #         self.__images.append(image)

    # def set_active_image(self, index):
    #     return self.__images[index]

    def set_sound(self,file_name):
        self.__sound = pg.mixer.Sound(os.path.join(get_sound_dir(),file_name))

    def play_sound(self,play):
        if play == True:
            self.sound.play(-1,0)
        else:
            self.sound.stop()

    @property
    def position(self):
        return self.__position;

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value
        
    @property
    def logger(self):
        return self.__log

    @property
    def screen(self):
        return self.__screen

    @property
    def image(self):
        return self.__image

    @property
    def size(self):
        return self.__size


