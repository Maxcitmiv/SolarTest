import json
import allure
from selene import browser


def attach_screenshot():
    png=browser.driver.get_screenshot_as_png()
    allure.attach(png,name='screenshot',attachment_type=allure.attachment_type.PNG)

def attach_page_source():
    html=browser.driver.page_source
    allure.attach(html,name='page_source',attachment_type=allure.attachment_type.HTML)

def attach_console_log():
    try:
        logs=browser.driver.get_log('browser')
        formatted_logs=json.dumps(logs,indent=2,ensure_ascii=False)
    except Exception as e:
        formatted_logs=f'Не удалось получить console logs: {e}'

    allure.attach(formatted_logs,name='console_log',attachment_type=allure.attachment_type.JSON)

def attach_video(video_url:str):
    allure.attach(video_url,name='video_url',attachment_type=allure.attachment_type.URI_LIST)
