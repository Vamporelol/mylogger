import logging
import logging.config
import os
from logging.handlers import TimedRotatingFileHandler
from time import sleep
from datetime import datetime

import logging


class AppLogger:
    def __init__(self):
        self._log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
        
    def get_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(logging.Formatter(self._log_format))
        return stream_handler

    def get_rotation_file_handler(self, filename):
        rotation_handler = TimedRotatingFileHandler('logs/' + filename, when='d', interval=1, 
                         backupCount=0)
        rotation_handler.setLevel(logging.DEBUG)
        rotation_handler.setFormatter(logging.Formatter(self._log_format))
        return rotation_handler


    def get_logger(self, filename, name):
        if not os.path.exists('logs/'):
            os.mkdir('logs')

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.get_stream_handler())
        logger.addHandler(self.get_rotation_file_handler(filename))
        return logger

