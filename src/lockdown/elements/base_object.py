import os,sys
import pygame
from pygame.locals import *
from lockdown.library import get_image_dir, get_sound_dir


class BaseObject(pygame.sprite.Sprite):

    def __init__(self,screen,size, name = "Base Object"):
        super(BaseObject,self).__init__()

        self.screen = screen
        self.pos = (0,0)
        self.size = size
        self.name = name
        self.image = ""
        self.sound = None

    def set_image_from_file(self,file_name,image_type = 0):
        # image_type 0 : regular ; 1 : with transparency
        
        img_file = os.path.join(get_image_dir(), file_name)

        if image_type == 0:
            temp_image = pygame.image.load(img_file).convert()
        else:
            temp_image = pygame.image.load(img_file)

        self.set_image(temp_image)

    def set_image(self,image):
        self.image =pygame.transform.scale(image,self.size)
        self.image.set_colorkey([250,250,0],RLEACCEL)
        self.rect = self.image.get_rect()

    def set_pos(self,pos):
        self.pos = pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def set_sound_from_file(self,file_name):
        #is_music = True will use mixer.Music
        self.sound = pygame.mixer.Sound(os.path.join(get_sound_dir(),file_name))

    def play_sound(self,play):
        if play == True:
            self.sound.play(-1,0)
        else:
            self.sound.stop()

    # def move(self,moving):
    #     self.moving = moving

    #     if self.sound != None:
    #         if self.moving == True:
    #             self.play_sound(True)
    #         else:
    #             self.play_sound(False)
