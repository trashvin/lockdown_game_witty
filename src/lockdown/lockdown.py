from logging import exception
import pygame as pg

from lockdown.library import *
from lockdown.constants import *
from lockdown.logger import Logger
from lockdown.screens.opening_screen import OpeningScreen
from lockdown.screens.game_screen import GameScreen
from lockdown.elements.paddle import Paddle
from lockdown.elements.ball import Ball

class Lockdown:
    
    def __init__(self, log : Logger):
        self.__log = log

        # initialize the pygame subsystem
        try:
            pg.init()
            pg.mixer.init()
            pg.font.init()

            pg.display.set_caption(f'{TEXT_GAME_TITLE} v{APP_VERSION}')
            self.screen = pg.display.set_mode(WINDOW_SIZE)

        except Exception as ex:
            self.__log.log(f'error initializing pygame. {ex}', level = 1)
            #  do system exit

        # create the screens and place it in a list
        opening_screen = OpeningScreen('opening screen', BLACK, self.screen, self.__log )
        game_screen = GameScreen('game screen', BLACK, self.screen, self.__log )
        self.screens = [opening_screen, game_screen]

        self.__current_screen = 0
        self.__level = 1

        # load and set starting position of paddle and ball
        paddle_loc = (((game_screen.game_area[1][0])/2-150/2), game_screen.game_area[1][1]-90)
        self.__paddle = Paddle(self.screen,(150,60), self.__log)
        self.__paddle.set_image(get_image('paddle_1.png'),1)
        self.__paddle.position = paddle_loc

        self.__ball = Ball(self.screen,(30,30), self.__log)
        self.__ball.set_image(get_image('ball_1.png'), 1)
        self.__ball.position = (paddle_loc[0]+65, paddle_loc[1]- 15)
        self.__ball.rect = self.__ball.rect.move((paddle_loc[0]+65, paddle_loc[1]- 15))


    def start(self):
        self.__log.log('starting the game ...')
        print('starting lockdown ...')
        
        # the main loop
        fps_clock = pg.time.Clock()
        direction_x = 1
        direction_y = -1
        anti_friction = 2
        level_start = False
        done = False
        while not done:
            fps_clock.tick(400)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    done = True 
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if self.__current_screen == 0:
                            self.__current_screen = 1
                        elif self.__current_screen == 1:
                            self.screens[self.__current_screen].hide_start_info()
                            level_start = True
                
            self.screens[self.__current_screen].show()

            if  self.__current_screen == 1:
                self.__draw_level_screen(self.__level)

            if level_start:
                mouse_xy = pg.mouse.get_pos()
                self.__paddle.move_with_mouse(mouse_xy,25,805-self.__paddle.size[0])

                if self.__ball.rect.right > 805:
                    direction_x = -1
                if self.__ball.rect.left < 30:
                    direction_x = 1
                if self.__ball.rect.top<30:
                    direction_y = 1
                if self.__ball.rect.bottom > 730:
                    direction_y = -1

                # self.__ball.position = (self.__ball.position[0]+direction_x, self.__ball.position[1]+ direction_y)
                self.__ball.rect = self.__ball.rect.move(
                    (direction_x * anti_friction, 
                    direction_y * anti_friction)
                )

            pg.display.flip()

        self.__log.log('quitting the game ...')
        pg.quit()

    def __draw_level_screen(self, level = 1):
        self.screen.blit(self.__paddle.image,self.__paddle.position) 
        self.screen.blit(self.__ball.image, self.__ball.rect)

# the main entry poinyt of the application
if __name__ == "__main__":
    log = Logger()
    log.log(f'initializing {APP_NAME} {APP_VERSION} ...')

    game = Lockdown(log)
    game.start()