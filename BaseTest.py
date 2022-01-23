import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    def get_url(self, url):
        self.driver.get(url)

    def click_element(self, element):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()

    def execute(self, script):
        self.driver.execute_script(script)

    def get_inner_text(self, element):
        el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element))
        text = el.get_attribute('innerText')
        return text
