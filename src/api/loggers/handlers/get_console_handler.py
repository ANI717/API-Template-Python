import sys
import logging
from logging import StreamHandler


def get_console_handler():
    formatter = logging.Formatter('%(asctime)s | %(request_id)s | %(levelname)s | %(message)s')
    
    handler = StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    
    return handler
