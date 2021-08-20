import os
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from datetime import datetime

""" 
class name : Logger
inherits from : none
purpose : this is a logger for logging operations 
"""
class Logger:
    
    def __init__(self):
        # copy trader main log
        self.__logger = logging.getLogger("lockdown_game")
        log_formatter = Formatter(fmt='%(asctime)s [%(levelname)s] : %(message)s',
                                  datefmt='%d-%b-%y %H:%M:%S')

        path = path = os.path.join(os.getcwd(), "lockdown_game.log")
        file_handler = RotatingFileHandler(path, maxBytes=1048576, backupCount = 10)

        file_handler.setFormatter(log_formatter)

        self.__logger.addHandler(file_handler)

        self.__logger.setLevel(10)
    
    """
    name : log
    parameters:
        message - the message to log
        level - integer value specifying the log level. see below
            1 - error
            2 - warning
            3 - information
            4 - debug
    """
    def log(self, message, level=3):
        if level == 1:
            self.__logger.error(message)
        elif level == 2:
            self.__logger.warning(message)
        elif level == 3:
            self.__logger.info(message)
        else:
            self.__logger.debug(message)
