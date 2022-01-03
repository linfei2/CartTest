import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from locators import Loc

@pytest.mark.usefixtures('init_driver')
class TestCart:

    @pytest.fixture()
    def add_to_cart(self):
        self.driver.get('https://moim.store/')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Loc.NEW_IN_BTN)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Loc.FIRST_PRODUCT)).click()
        self.driver.execute_script('window.scrollTo(0, 400)')
        sleep(1)
        self.driver.find_element(*Loc.ADD_TO_CART_BTN).click()

    def test_add_to_cart(self, add_to_cart):
        sleep(1)
        cart_count = self.driver.find_element(*Loc.CART_ICON)
        assert cart_count.get_attribute('innerText') == '1'

    def test_remove_from_cart(self, add_to_cart):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Loc.REMOVE_BTN)).click()
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Loc.EMPTY_CART_NOTIFICATION))
        assert message.get_attribute('innerText') == "Twój koszyk aktualnie jest pusty."
