import os,sys
from typing import TYPE_CHECKING
import pygame
from pygame.locals import *
from lockdown.library import *
from lockdown.elements.base_object import BaseObject

class Ball(BaseObject):

    def __init__(self, screen, size, logger, name = 'Ball'):
        super().__init__(screen, size, logger, name)
        self.logger.log('initializing a ball')

        self.__direction_x = 1
        self.__direction_y = 1

    def collides_with(self, element):
        pass

    

    