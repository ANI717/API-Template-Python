import sys
import logging


def get_console_handler():
    formatter = logging.Formatter('%(asctime)s | %(request_id)s | %(levelname)s | %(message)s')
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    
    return handler
