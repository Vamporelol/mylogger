import os
from datetime import datetime

import pytest

from app_logger import AppLogger

def test_logging():
    
    filename = datetime.today().strftime('%d-%m-%Y') + '.log'
    log = AppLogger().get_logger(filename, __name__)
    for i in range(0, 3):
        log.debug('test')                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    assert os.path.exists('logs/')
    assert os.path.exists('logs/' + filename)
    
