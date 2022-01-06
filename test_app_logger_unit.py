from os.path import abspath
from datetime import datetime
from logging import Logger, StreamHandler, DEBUG
from logging.handlers import TimedRotatingFileHandler

from pytest import raises

from app_logger import AppLogger 

def test_get_file_handler():
    filename = datetime.today().strftime('%d-%m-%Y') + '.log'
    fileway = 'logs/' + datetime.today().strftime('%d-%m-%Y') + '.log'
    handler = AppLogger().get_rotation_file_handler(filename)

    assert isinstance(handler, TimedRotatingFileHandler)
    assert handler.level == DEBUG
    assert handler.baseFilename == abspath(fileway)


def test_get_stream_handler():
    handler = AppLogger().get_stream_handler()

    assert isinstance(handler, StreamHandler)
    assert handler.level == DEBUG

def test_get_logger():
    filename = datetime.today().strftime('%d-%m-%Y') + '.log'
    logger = AppLogger().get_logger(filename, __name__)

    assert isinstance(logger, Logger)
    assert logger.name == __name__
    assert len(logger.handlers) == 2              

def test_get_logger_call_without_name():
    with raises(TypeError):
        AppLogger().get_logger()
