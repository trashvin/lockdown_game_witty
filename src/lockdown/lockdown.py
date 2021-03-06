from logging import exception
import pygame as pg

import lockdown.library
import lockdown.constants
from lockdown.constants import *
from lockdown.logger import Logger
from lockdown.screens.opening_screen import OpeningScreen
from lockdown.screens.game_screen import GameScreen
from lockdown.elements.paddle  import Paddle
from lockdown.elements.ball import Ball
from lockdown.library import *
from lockdown.elements.virus import Virus
from lockdown.elements.brick import Brick
from lockdown.screens.ending_screen import EndingScreen

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
        
        self.initialize()

    def set_level(self, level):
        self.__level = level
        
    def initialize(self):
        opening_screen = OpeningScreen('opening screen', BLACK, self.screen, self.__log)
        game_screen = GameScreen('game screen', (33,33,33), self.screen, self.__log)
        end_screen = EndingScreen('opening screen', BLACK, self.screen, self.__log)

        self.screens = [opening_screen, game_screen, end_screen]
        self.__current_screen = 0
        self.__level = 1
        self.__virus_count = 0

        self.__initialize_ball_paddle_location()

        self.__level_layout = retrieve_level_layout(self.__level)
        self.__elements = []
        self.__initialize_elements()
        self.__score = 0
        self.__life = 3
        self.__wall_bounce_sound = self.__bounce_sound = pg.mixer.Sound(get_sound(WALL_BOUNCE))

    def __initialize_ball_paddle_location(self):
        game_screen = self.screens[1]
        paddle_loc = (((game_screen.game_area[1][0])/2-150/2), game_screen.game_area[1][1]-90)
        self.__paddle = Paddle(self.screen,(150,60), self.__log)
        self.__paddle.set_image(get_image('paddle_1.png'),1)
        self.__paddle.rect = self.__paddle.rect.move(paddle_loc)
        self.__start_loc_paddle = paddle_loc

        self.__ball = Ball(self.screen,(30,30), self.__log)
        self.__ball.set_image(get_image('ball_1.png'), 1)
        self.__ball.rect = self.__ball.rect.move((paddle_loc[0]+65, paddle_loc[1]- 15))
        self.__start_loc_ball = (paddle_loc[0]+65, paddle_loc[1]- 15)

    def next_level(self):
        self.__current_screen = 1
        self.__level += 1
        self.__virus_count = 0

        self.__initialize_ball_paddle_location()

        self.__level_layout = retrieve_level_layout(self.__level)
        self.__elements = []
        self.__initialize_elements()
        self.__life = 3
        self.__wall_bounce_sound = self.__bounce_sound = pg.mixer.Sound(get_sound(WALL_BOUNCE))

        
    def __initialize_elements(self):
        x = 40
        y = 50
        for row in self.__level_layout:
            element_row = []
            for element in row:
                if int(element) < 10:
                    virus = Virus(self.screen, (50,50),self.__log, int(element))
                    virus.rect = virus.rect.move((x,y))
                    element_row.append(virus)
                    self.__virus_count +=1
                else:
                    brick = Brick(self.screen, (50,50),self.__log, int(element))
                    brick.rect = brick.rect.move((x,y))
                    element_row.append(brick)

                x += 50
            x = 40
            y += 50    
            self.__elements.append(element_row)


    def start(self):
        self.__log.log('starting the game ...')
        
        # the main loop
        fps_clock = pg.time.Clock()
        direction_x = 1
        direction_y = -1
        anti_friction = ANTI_FRICTION
        level_status = 0
        ball_dead = False
        done = False
        while not done:
            fps_clock.tick(FPS)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    done = True 
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if self.__current_screen == 0:
                            self.screens[self.__current_screen].exit()
                            self.__current_screen = 1
                        elif self.__current_screen == 1:
                            if level_status == 0:
                                self.screens[self.__current_screen].hide_start_info()
                                level_status = 1
                            else:
                                if ball_dead:
                                    self.screens[self.__current_screen].restart_life(False)
                                    ball_dead = False
                    
                    elif event.key == pg.K_RETURN:
                        if self.__current_screen == 2:
                            if level_status == 3:
                                self.__log.log('restarting game ....')
                                self.initialize()
                                self.start()
                                
                                # self.__level += 1
                        if self.__current_screen == 1:
                            if level_status == 4:
                                self.screens[self.__current_screen].show_completed_message(0)
                                self.__log.log('advancing to a new level..')
                                self.next_level()
                                self.start()

                    elif event.key == pg.K_ESCAPE:
                        if self.__current_screen == 1:
                            if level_status >= 3:
                                done = True
                                continue
                    
            self.screens[self.__current_screen].show() 
            
            # logic when screen is in game screen
            if  self.__current_screen == 1:
                # get the game area
                game_area = self.screens[self.__current_screen].game_area
                # draw the elements
                self.__draw_level_screen(self.__level)

                # if level has started , start the game
                if level_status == 1:
                    
                    # move the paddle based on the mouse location
                    mouse_x = pg.mouse.get_pos()[0]
                    self.__paddle.move_with_mouse(
                        (mouse_x,GAME_SCREEN_END[1]-75),
                        25+self.__paddle.size[0]/2,805-self.__paddle.size[0]/2
                    )
                    
                    if not ball_dead:   
                         
                        if self.__ball.rect.right > game_area[1][0]:
                            direction_x = -1
                            pg.mixer.Channel(0).play(self.__wall_bounce_sound)
                        if self.__ball.rect.left < game_area[0][0]:
                            direction_x = 1
                            pg.mixer.Channel(0).play(self.__wall_bounce_sound)
                        if self.__ball.rect.top<game_area[0][1]:
                            direction_y = 1
                            pg.mixer.Channel(0).play(self.__wall_bounce_sound)
                        if self.__ball.rect.bottom > game_area[1][1]:
                            direction_y = -1
                            pg.mixer.Channel(0).play(self.__wall_bounce_sound)
                            ball_dead = True
                            self.__life -= 1
                            self.screens[self.__current_screen].set_life(self.__life)

                            # if all lives are spent, lockdown! else, just continue playing
                            if self.__life == 0:
                                self.__log.log('game over, lockdown!')
                                level_status = 3
                                self.__current_screen += 1
                                self.screens[self.__current_screen].show(False)
                            else:
                                self.__log.log('game continues with reduced life')
                                self.screens[self.__current_screen].restart_life(True)


                        # check if ball and padd made contact
                        if self.__ball.rect.colliderect(self.__paddle.rect):
                            direction_y = -1

                        # check if the ball comes in contact with the elements
                        # TODO: the logic is not perfect, improve it!
                        for element_row in self.__elements:
                            for element in element_row:
                                if self.__ball.rect.colliderect(element.rect):
                                    if element.name == 'Virus' and element.visible == True: 
                                        element.hit()
                                        self.__score += element.points
                                        self.screens[self.__current_screen].set_score(self.__score)
                                        
                                        # TODO :  improve this!
                                        direction_y *= -1

                                        # lets make sure we have a count of active viruses
                                        if element.visible == False:
                                            self.__virus_count -= 1

                                        # if the virus count is zero, lets end the level
                                        if self.__virus_count == 0:
                                            if self.__level == MAX_LEVEL:
                                                level_status = 5
                                                # show game completed
                                                self.__current_screen += 1
                                                self.screens[self.__current_screen].show(True)
                                            else:
                                                level_status = 4
                                                # show level completed
                                                self.screens[self.__current_screen].show_completed_message(LEVEL_COMPLETE)
                                    
                                    elif element.name == 'Brick':
                                        element.hit()
                                        direction_y *= -1

                        # lets move the ball
                        self.__ball.rect = self.__ball.rect.move(
                            (direction_x * anti_friction, 
                            direction_y * anti_friction)
                        )

                    else:
                        self.__ball.rect = self.__ball.image.get_rect()
                        self.__ball.rect = self.__ball.rect.move(self.__start_loc_ball)
                        self.__paddle.rect = self.__paddle.image.get_rect()
                        self.__paddle.rect = self.__paddle.rect.move(self.__start_loc_paddle)

            pg.display.flip()   

        self.__log.log('quitting the game ...')
        pg.quit()

    def __draw_level_screen(self, level = 1):
        self.screen.blit(self.__paddle.image,self.__paddle.rect) 
        
        for element_row in self.__elements:
            for element in element_row:
                if element.name == 'Virus' and element.visible == True:
                    self.screen.blit(element.image, element.rect)
                elif element.name == 'Brick' :
                    self.screen.blit(element.image, element.rect)
        self.screen.blit(self.__ball.image, self.__ball.rect)



# the main entry poinyt of the application
if __name__ == "__main__":
    log = Logger()
    log.log(f'initializing {APP_NAME} {APP_VERSION} ...')

    game = Lockdown(log)
    game.start()