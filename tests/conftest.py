import pytest
from selene import browser


@pytest.fixture
def browser_configuration():
    browser.config.browser_name = "chrome"
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 720

    yield

    browser.quit()
