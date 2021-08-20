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

    def get_resulting_direction(self, current_dir, element):
        element_rect = element.rect
        if self.rect.top <= element_rect.bottom:
            return (current_dir[0],-1)
        elif self.rect.bottom >= element_rect.top:
            return (current_dir[0],1)

    