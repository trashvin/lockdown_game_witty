import os,sys
import pygame as pg
from pygame.locals import *
from lockdown.constants import *
from lockdown.library import *
from lockdown.elements.base_object import BaseObject

class Brick(BaseObject):

    def __init__(self, screen, size, logger, type : int, name = 'Brick'):
        super().__init__(screen, size, logger, name)
        self.logger.log('initializing a brick')
        self.__type = type-10
        self.__has_power = True if self.__type == 1 or self.__type == 3 else False
        self.__image = BRICK_IMAGE[type-10]
        self.__visible = True
        self.set_image(self.__image, 1)
        self.__bounce_sound = pg.mixer.Sound(get_sound(BRICK_BOUNCE))

    def hit(self):
        self.logger.log(f'{self.name} was hit')
        pg.mixer.Channel(0).play(self.__bounce_sound)

    @property
    def visible(self):
        return self.__visible





    
