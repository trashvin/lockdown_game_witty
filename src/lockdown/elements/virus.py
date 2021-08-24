import os,sys
import pygame as pg
from pygame.locals import *
from lockdown.constants import *
from lockdown.library import *
from lockdown.elements.base_object import BaseObject

class Virus(BaseObject):

    def __init__(self, screen, size, logger, type : int, name = 'Virus'):
        super().__init__(screen, size, logger, name)
        self.logger.log('initializing a virus')
        self.__type = type-1
        self.__points = VIRUS_POINTS[type-1]
        self.__hit_life = VIRUS_HIT_LIFE[type-1]
        self.__image = VIRUS_IMAGE[type-1]
        self.__visible = True
        self.set_image(self.__image, 1)

        self.__bounce_sound = pg.mixer.Sound(get_sound(VIRUS_BOUNCE))
        self.__kill_sound = pg.mixer.Sound(get_sound(VIRUS_KILL))

    def hit(self):
        self.logger.log('a virus was hit',4)
        self.__hit_life -= 1
        if self.__hit_life == 0:
            self.logger.log('a virus was killed',4)
            self.__visible = False
            pg.mixer.Channel(0).play(self.__kill_sound)
        else:
            pg.mixer.Channel(0).play(self.__bounce_sound)

        
    @property
    def visible(self):
        return self.__visible

    @property
    def points(self):
        return self.__points


    
