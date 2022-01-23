import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome', 'firefox'])
def init_driver(request):
    if request.param == 'chrome':
        s = Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=s)
    else:
        s = Service(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=s)
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.close()
    web_driver.quit()

