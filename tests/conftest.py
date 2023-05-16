import pytest
from selene import browser

from utilites import attach


@pytest.fixture
def browser_configuration():
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
