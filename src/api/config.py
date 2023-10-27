from typing import Union
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

from api.loggers.custom_logger import custom_logger


load_dotenv()
load_dotenv(find_dotenv("../.env"))


REQUEST_ID = None


class Settings(BaseSettings):
    ENV : str = "dev"
    ROOT_PATH : Union[str, None] = None

settings = Settings()

logger = custom_logger(console_handler=True,
                       file_handler=True,
                       filename="logfile.log",
                       when="midnight",)
