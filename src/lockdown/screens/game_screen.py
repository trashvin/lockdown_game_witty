import pygame as pg
from lockdown.constants import * 
from lockdown.library import get_font, get_image
from lockdown.screens.base_screen import BaseScreen

class GameScreen(BaseScreen):

    def __init__(self, name, bg_color, screen, logger, level = 1):
        super().__init__(name, bg_color, screen, logger)
        self.logger.log(f'initializing the game screen. level = {level}')
        self.__load_images()
        self.__show_start_info = True
        self.__title_font = pg.font.Font(get_font('minecraft.otf'), 70)
        self.__title = self.__title_font.render(f'LEVEL {level}',1, WHITE)
        self.__inst1_font = pg.font.SysFont("calibri", 20)
        self.__instruction = self.__inst1_font.render(TEXT_LEVEL_START,1, WHITE)

        self.__game_area = ((30,30),(805,748))

    def show(self):
        screen_width = WINDOW_SIZE[0]
        screen_height = WINDOW_SIZE[1]

        self.screen.fill(self.bg_color)

        self.screen.blit(self.__bg_image,(0,0))
        for x in range(0,800, 30):
            self.screen.blit(self.__lwall_image,(0,x))
        
        for x in range(0,1024, 30):
            self.screen.blit(self.__lwall_image,(x,0))
            
        # self.screen.blit(self.__rwall_image,(975,0))

        for x in range(0,1024,30):
            self.screen.blit(self.__lwall_image,(x,750))

        for y in [805,835,865,895,925,955,985,1015]:
            for x in range(0,800, 30):
                self.screen.blit(self.__rwall_image,(y,x))

        if self.__show_start_info:
            self.screen.blit(self.__title,
                (screen_width/2 - self.__title.get_width()/2 - 100, screen_height/2 - self.__title.get_height()/2-300))
            self.screen.blit(self.__instruction,
                (screen_width/2 - self.__instruction.get_width()/2 - 100, screen_height - 20))

    def hide_start_info(self):
        self.__show_start_info = False   

    def __load_images(self):
        self.__rwall_image = pg.image.load(get_image('wall_tile_right.png'))
        self.__rwall_image = pg.transform.scale(self.__rwall_image,(30,30))
        self.__lwall_image = pg.image.load(get_image('wall_tile_left.png'))
        self.__lwall_image = pg.transform.scale(self.__lwall_image,(30,30))

        self.__bg_image = pg.image.load(get_image('bg_image1.png'))
        self.__bg_image = pg.transform.scale(self.__bg_image,WINDOW_SIZE)

    @property
    def game_area(self):
        return self.__game_area
