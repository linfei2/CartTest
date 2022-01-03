import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def init_driver(request):
    s = Service(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=s)
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.close()
    web_driver.quit()

