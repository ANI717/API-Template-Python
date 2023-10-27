import logging


def get_file_handler(filename="logfile.log", when="midnight"):
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    
    handler = logging.handlers.TimedRotatingFileHandler(filename=filename, when=when)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    
    return handler
