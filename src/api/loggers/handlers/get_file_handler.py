import logging
from logging.handlers import TimedRotatingFileHandler


def get_file_handler(filename="logfile.log", when="midnight"):
    formatter = logging.Formatter('%(asctime)s | %(request_id)s | %(levelname)s | %(message)s')
    
    handler = TimedRotatingFileHandler(filename=filename, when=when)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    
    return handler
