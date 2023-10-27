import logging
from api.loggers.handlers.get_file_handler import get_file_handler
from api.loggers.handlers.get_console_handler import get_console_handler
from api.middlewares.generate_request_id import Request_ID


class SystemLogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, "request_id"):
            record.request_id = Request_ID.REQUEST_ID
        return True


def custom_logger(console_handler=True,
                  file_handler=True,
                  filename="logfile.log",
                  when="midnight",):
    
    logger = logging.getLogger("api-logger")
    logger.setLevel(logging.INFO)
    
    if console_handler:
        logger.addHandler(get_console_handler())
    
    if file_handler:
        logger.addHandler(get_file_handler(filename=filename, when=when))
    
    logger.addFilter(SystemLogFilter())
    logger.propagate = False
    
    return logger
