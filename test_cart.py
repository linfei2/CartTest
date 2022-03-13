import pytest
from base_class import BaseClass
from time import sleep
from locators import Loc


class TestCart(BaseClass):

    @pytest.fixture()
    def add_to_cart(self):
        self.get_url('https://moim.store/')
        self.click_element(Loc.NEW_IN_BTN)
        self.click_element(Loc.FIRST_PRODUCT)
        self.execute('arguments[0].scrollIntoView();', self.find(Loc.ADD_TO_CART_BTN))
        sleep(1)
        self.click_element(Loc.ADD_TO_CART_BTN)

    def test_add_to_cart(self, add_to_cart):
        count = self.get_value(Loc.CART_ICON)
        assert count == '1'

    def test_remove_from_cart(self, add_to_cart):
        self.click_element(Loc.REMOVE_BTN)
        message = self.get_value(Loc.EMPTY_CART_NOTIFICATION)
        assert message == "Twój koszyk aktualnie jest pusty."
