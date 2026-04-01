import pytest
from selene import browser
from selenium.webdriver.remote.client_config import ClientConfig

from utils.attach import attach_video, attach_screenshot,attach_console_log,attach_page_source
from selenium import webdriver
from config.settings import *

SELENOID_URL='https://selenoid.autotests.cloud/wd/hub'
VIDEO_BASE_URL='https://selenoid.autotests.cloud/video'

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report=outcome.get_result()
    setattr(item,f'rep_{report.when}',report)

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
        command_executor=SELENOID_URL,
        options=options,
        client_config=ClientConfig(
            remote_server_addr=SELENOID_URL,
            username=LOGIN,
            password=PASSWORD,
        ),
    )
    browser.config.driver=driver
    browser.config.base_url = 'https://rt-solar.ru'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield


    attach_screenshot()
    attach_console_log()
    attach_page_source()

    driver.quit()

    video_url=f'{VIDEO_BASE_URL}/{video_name}'
    attach_video(video_url)