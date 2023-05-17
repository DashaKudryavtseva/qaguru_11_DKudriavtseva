import os

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utilites import attach
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption('--browser-version', default='100.0')


DEFAULT_BROWSER_VERSION = '100.0'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_configuration(request):
    browser_version = request.config.getoption('--browser-version')

    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": DEFAULT_BROWSER_VERSION,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    browser.config.browser_name = "chrome"
    browser.config.base_url = 'https://demoqa.com'

    browser.config.window_height = 1080
    browser.config.window_width = 720

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
