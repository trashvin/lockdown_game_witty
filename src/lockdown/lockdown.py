from logging import exception
import pygame as pg

import lockdown.library
import lockdown.constants
from lockdown.constants import APP_NAME, APP_VERSION
from lockdown.logger import Logger



class Lockdown:
    
    def __init__(self, log : Logger):
        self.__log = log

        # initialize the pygame subsystem
        try:
            pg.init()
            pg.mixer.init()
            pg.font.init()
        except Exception as ex:
            self.__log.log(f'error initializing pygame. {ex}', level = 1)
            #  do system exit


    def start(self):
        self.__log.log('starting the game ...')
        print('starting lockdown ...')


# the main entry poinyt of the application
if __name__ == "__main__":
    log = Logger()
    log.log(f'initializing {APP_NAME} {APP_VERSION} ...')

    game = Lockdown(log)
    game.start()