
import pygame as pg
from lockdown.constants import * 
from lockdown.library import *
from lockdown.screens.base_screen import BaseScreen

"""
class name : GameScreen
inherits from : BaseScreen
purpose : the main game screen
"""
class GameScreen(BaseScreen):

    def __init__(self, name, bg_color, screen, logger, level = 1):
        super().__init__(name, bg_color, screen, logger)
        
        self.logger.log(f'initializing {name} ...')

        self.__game_area = (GAME_SCREEN_START,GAME_SCREEN_END)
        self.__level = level
        self.__score = 0
        self.__life = 3

        self.__show_start_info = True
        self.__restart_life = False
        self.__show_lockdown_msg = False   
        self.__show_level_completed_msg = False
        self.__show_game_completed_msg = False

        self.__load_texts()
        self.__load_images()
        self.__load_sounds()

    @property
    def game_area(self):
        return self.__game_area

    def show(self):
        screen_width = WINDOW_SIZE[0]
        screen_height = WINDOW_SIZE[1]

        self.screen.fill(self.bg_color)
        self.screen.blit(self.__bg_image,(0,0))
        
        for x in range(0,screen_width, 30):
            self.screen.blit(self.__lwall_image,(0,x))
        
        for x in range(0,screen_width, 30):
            self.screen.blit(self.__lwall_image,(x,0))

        for x in range(0,screen_width,30):
            self.screen.blit(self.__lwall_image,(x,750))

        for y in [805,835,865,895,925,955,985,1015]:
            for x in range(0,800, 30):
                self.screen.blit(self.__rwall_image,(y,x))

        self.screen.blit(self.__lockdown_small,(825, 30))
        self.screen.blit(self.__map_image,(825,70))

        self.screen.blit(self.__score_board,(825,550))
        self.screen.blit(self.__score_text, (835, 560))
        self.screen.blit(self.__life_text, (835,610))

        # score
        self.__score_text1 = pg.font.Font(get_font('retro1.ttf'), 40)
        self.__score_text1 = self.__score_text1.render(str(self.__score),1, Y_GREEN)
        self.screen.blit(self.__score_text1, (835, 580))
        
        # life 
        self.__life_text1 = pg.font.Font(get_font('retro1.ttf'), 40)
        self.__life_text1 = self.__life_text1.render(str(self.__life),1, Y_GREEN)
        self.screen.blit(self.__life_text1, (835, 630))


        if self.__show_start_info:
            self.screen.blit(self.__title,
                (screen_width/2 - self.__title.get_width()/2 - 100, 
                 screen_height/2 - self.__title.get_height()/2 + 100))
            self.screen.blit(self.__instruction,
                (screen_width/2 - self.__instruction.get_width()/2 - 100, screen_height - 20))

        if self.__restart_life:
            self.screen.blit(self.__instruction,
                (screen_width/2 - self.__instruction.get_width()/2 - 100, screen_height - 20))
        
        self.__sound.play(-1)

        if self.__show_lockdown_msg:
            self.screen.blit(self.__lockdown_board,(100,400))
            self.screen.blit(self.__lockdown_msg,(230,425))
            self.screen.blit(self.__restart_msg,(235,520))
            self.screen.blit(self.__quit_msg,(260,550))
            self.screen.blit(self.__future_msg,(180,580))
            # pg.mixer.Channel(0).play(self.__lockdown_sound)

        if self.__show_level_completed_msg:
            self.screen.blit(self.__completion_board,(100,400))
            self.screen.blit(self.__level_complete_msg,(250,435))
            self.screen.blit(self.__next_level_msg,(235,540)) 
            self.screen.blit(self.__future_msg,(195,580))

        if self.__show_game_completed_msg:
            self.screen.blit(self.__completion_board,(100,400))
            self.screen.blit(self.__game_complete_msg,(250,435))
            self.screen.blit(self.__restart_msg,(235,520))
            self.screen.blit(self.__quit_msg,(260,550))
            self.screen.blit(self.__future_msg,(195,580))

    def exit(self):
        self.__sound.stop()

    def set_score(self, value):
        self.__score = value

    def set_life(self, value):
        self.__life = value

    def restart_life(self, value):
        self.__restart_life = value

    def set_lockdown(self, value):
        self.__show_lockdown_msg = value

    def show_completed_message(self, completed_type = 1):
        if completed_type == 1:
            self.__show_level_completed_msg = True
        elif completed_type == 2:
            self.__show_game_completed_msg = True
        else:
            self.__show_level_completed_msg = False
            self.__show_game_completed_msg = False

    def hide_start_info(self):
        self.__show_start_info = False

    def __load_images(self):
        self.__rwall_image = pg.image.load(get_image('wall_tile_right.png'))
        self.__rwall_image = pg.transform.scale(self.__rwall_image,(30,30))
        self.__lwall_image = pg.image.load(get_image('wall_tile_left.png'))
        self.__lwall_image = pg.transform.scale(self.__lwall_image,(30,30))

        self.__bg_image = pg.image.load(get_image('bg_image2.png'))
        self.__bg_image = pg.transform.scale(self.__bg_image,WINDOW_SIZE)

        self.__score_board = pg.Surface((160, 130))
        self.__score_board.fill(BLACK)

        self.__lockdown_board = pg.Surface((650, 230))
        self.__lockdown_board.fill(RED)

        self.__completion_board = pg.Surface((650, 230))
        self.__completion_board.fill(GREEN)

        self.__map_image = pg.image.load(get_image('map.jpg'))
        self.__map_image = pg.transform.scale(self.__map_image,(160,100))

    def __load_sounds(self):
        self.__sound = pg.mixer.Sound(get_sound(BG_MUSIC))
        self.__sound.set_volume(0.05)
    
    def __load_texts(self):
        # load the text
        self.__title_font = pg.font.Font(get_font(FONT_MAIN_1), 70)
        self.__title = self.__title_font.render(f'LEVEL {self.__level}',1, WHITE)

        self.__inst1_font = pg.font.SysFont(FONT_SUB_1, 18)
        self.__instruction = self.__inst1_font.render(TEXT_LEVEL_START,1, WHITE)

        self.__lockdown_msg = pg.font.Font(get_font(FONT_MAIN_1), 70)
        self.__lockdown_msg = self.__lockdown_msg.render(APP_NAME,1, WHITE)

        self.__level_complete_msg = pg.font.Font(get_font(FONT_MAIN_1), 40)
        self.__level_complete_msg = self.__level_complete_msg.render(TEXT_LEVEL_COMPLETE,1, WHITE)

        self.__game_complete_msg = pg.font.Font(get_font(FONT_MAIN_1), 40)
        self.__game_complete_msg = self.__game_complete_msg.render(TEXT_GAME_COMPLETE,1, WHITE)

        self.__restart_msg = pg.font.SysFont(FONT_SUB_1, 25)
        self.__restart_msg = self.__restart_msg.render(TEXT_ENTER_RESTART,1, GRAY)

        self.__next_level_msg = pg.font.SysFont(FONT_SUB_1, 25)
        self.__next_level_msg = self.__next_level_msg.render(TEXT_ENTER_NEXT,1, GRAY)

        self.__quit_msg = pg.font.SysFont(FONT_SUB_1, 25)
        self.__quit_msg = self.__quit_msg.render(TEXT_ESC_QUIT,1, GRAY)

        self.__future_msg = pg.font.SysFont(FONT_SUB_1, 25)
        self.__future_msg = self.__future_msg.render(TEXT_FUTURE,1, GRAY)

        self.__score_text = pg.font.SysFont(FONT_SUB_1, 28)
        self.__score_text = self.__score_text.render(TEXT_SCORE,1, GREEN)

        self.__life_text = pg.font.SysFont(FONT_SUB_1, 28)
        self.__life_text = self.__life_text.render(TEXT_LIFE,1, GREEN)

        self.__lockdown_small = pg.font.Font(get_font(FONT_MAIN_1), 30)
        self.__lockdown_small = self.__lockdown_small.render(APP_NAME,1, WHITE)

        
