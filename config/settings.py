import os

import pydantic_settings
from dotenv import load_dotenv
import pydantic
from pydantic import HttpUrl

load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")

class Config(pydantic_settings.BaseSettings):
    base_url: HttpUrl = 'https://rt-solar.ru'
    window_width: int = 1920
    window_height: int = 1080
    SELENOID_URL: HttpUrl = 'https://selenoid.autotests.cloud/wd/hub'
    VIDEO_BASE_URL: HttpUrl = 'https://selenoid.autotests.cloud/video'




