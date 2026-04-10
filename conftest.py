import pytest
from selene import browser
from selenium.webdriver.remote.client_config import ClientConfig

from utils.attach import attach_video, attach_screenshot, attach_console_log, attach_page_source
from selenium import webdriver
from config.settings import *

config_pydantic=Config()

@pytest.fixture(autouse=True)
def browser_function(request):
    test_name=request.node.name
    video_name=f'{test_name}.mp4'
    options = webdriver.ChromeOptions()

    options.set_capability("browserName", "chrome")
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    options.set_capability("selenoid:options", {
        "enableVideo": True,
        "enableVNC": True,
        "name": test_name,
        "videoName": video_name,
    })

    driver = webdriver.Remote(
        command_executor=str(config_pydantic.SELENOID_URL),
        options=options,
        client_config=ClientConfig(
            remote_server_addr=str(config_pydantic.SELENOID_URL),
            username=LOGIN,
            password=PASSWORD,
        ),
    )
    browser.config.driver=driver
    browser.config.base_url = str(config_pydantic.base_url)
    browser.config.window_width = config_pydantic.window_width
    browser.config.window_height = config_pydantic.window_height

    yield


    attach_screenshot()
    attach_console_log()
    attach_page_source()

    driver.quit()

    video_url=f'{str(config_pydantic.VIDEO_BASE_URL)}/{video_name}'
    attach_video(video_url)
