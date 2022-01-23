import pytest
from BaseTest import BaseTest
from time import sleep
from locators import Loc


class TestCart(BaseTest):

    @pytest.fixture()
    def add_to_cart(self):
        self.get_url('https://moim.store/')
        self.click_element(Loc.NEW_IN_BTN)
        self.click_element(Loc.FIRST_PRODUCT)
        self.execute('window.scrollTo(0, 400)')
        sleep(1)
        self.click_element(Loc.ADD_TO_CART_BTN)

    def test_add_to_cart(self, add_to_cart):
        sleep(1)
        count = self.get_inner_text(Loc.CART_ICON)
        assert count == '1'

    def test_remove_from_cart(self, add_to_cart):
        self.click_element(Loc.REMOVE_BTN)
        message = self.get_inner_text(Loc.EMPTY_CART_NOTIFICATION)
        assert message == "Twój koszyk aktualnie jest pusty."
