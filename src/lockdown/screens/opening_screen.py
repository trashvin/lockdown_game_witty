import pygame as pg
from lockdown.constants import * 
from lockdown.library import *
from lockdown.screens.base_screen import BaseScreen


"""
class name : OpeningScreen
inherits from : BaseScreen
purpose : opening screen
"""
class OpeningScreen(BaseScreen):
    
    def __init__(self, name, bg_color, screen, logger):
        super().__init__(name, bg_color, screen, logger)
        self.logger.log(f'initializing {name}...')

        self.__bg_image = pg.image.load(get_image('opening_bg.png'))
        self.__bg_image = pg.transform.scale(self.__bg_image,WINDOW_SIZE)

        self.__title_font = pg.font.Font(get_font(FONT_MAIN_1), 120)
        self.__title = self.__title_font.render(TEXT_GAME_TITLE,1, RED)

        self.__inst1_font = pg.font.SysFont(FONT_SUB_1, 30)
        self.__instruction = self.__inst1_font.render(TEXT_OPENING_SCREEN_INTS1,1, WHITE)

        self.__sound = pg.mixer.Sound(get_sound(INTRO_MUSIC))
        self.__sound.set_volume(0.5)

    """
    name : show
    purpose : show the objects on the screen
    """
    def show(self): 
        screen_width = WINDOW_SIZE[0]
        screen_height = WINDOW_SIZE[1]

        try:
            self.screen.blit(self.__bg_image,(0,0))
            self.screen.blit(self.__title,
                (screen_width/2 - self.__title.get_width()/2, screen_height/2 - self.__title.get_height()/2))
            self.screen.blit(self.__instruction,
                (screen_width/2 - self.__instruction.get_width()/2, screen_height - 40))

            self.__sound.play(-1)
        except:
            pass
    
    """
    name : exit
    purpose : do steps when transitioning to another screen
    """
    def exit(self):
        self.__sound.stop()
        
