import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_config():
    browser.config.base_url = 'https://rt-solar.ru'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
