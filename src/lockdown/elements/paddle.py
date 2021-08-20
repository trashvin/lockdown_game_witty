import os,sys
import pygame
from pygame.locals import *
from lockdown.library import *
from lockdown.elements.base_object import BaseObject

class Paddle(BaseObject):

    def __init__(self, screen, size, logger, name = 'Paddle'):
        super().__init__(screen, size, logger, name)
        self.logger.log('initializing a paddle')

    '''
    method that allows the paddle to follow the X movement of the mouse 
    this happens only when the mouse pointer is in the game area
    '''
    def move_with_mouse(self, mouse_xy, start_x, end_x):
        try:
            if mouse_xy[0] >= start_x and mouse_xy[0] <= end_x:
                self.rect.center = mouse_xy
        except Exception as ex:
            pass

        