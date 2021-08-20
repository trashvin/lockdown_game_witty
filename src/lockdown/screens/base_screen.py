from lockdown.logger import Logger

"""
class name: BaseScreen
inherits from: none
purpose : base class for all screens
"""
class BaseScreen:
    def __init__(self, name, bg_color, screen, logger):
        self.__name = name
        self.__bg_color = bg_color
        self.__screen = screen
        self.__log = logger

    @property
    def screen(self):
        return self.__screen

    @property
    def logger(self):
        return self.__log

    @property
    def bg_color(self):
        return self.__bg_color
    