import os,sys
import pygame
from pygame.locals import *
from lockdown.library import *
from lockdown.elements.base_object import BaseObject

class Paddle(BaseObject):

    def __init__(self, screen, size, logger, name = 'Paddle'):
        super().__init__(screen, size, logger, name)
        self.logger.log('initializing a paddle')

    def move_with_mouse(self, mouse_xy, start_x, end_x):
        if mouse_xy[0] >= start_x and mouse_xy[0] <= end_x:
            new_pos = (mouse_xy[0], self.position[1])
            self.position = new_pos

        