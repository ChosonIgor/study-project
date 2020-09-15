from .base_page import BasePage
from .locators import AddToBasket, ProductPageLocators
# import time


class ProductPage(BasePage):
    def adding_goods(self):
        button_add_to_basket = self.browser.find_element(*AddToBasket.ADD_TO_BASKET)
        button_add_to_basket.click()

    def check_of_goods(self):
        name_goods = self.browser.find_element(*AddToBasket.NAME_GOODS).text
        price_goods = self.browser.find_element(*AddToBasket.PRICE_GOODS).text
        assert name_goods == self.browser.find_element(*AddToBasket.GOODS_IN_BASKET).text, "False in goods name"
        assert price_goods == self.browser.find_element(*AddToBasket.PRICE_IN_BASKET).text, "False in goods price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappeared_element(self):
        assert self.is_disappeared(*ProductPageLocators.ANY_ELEMENT), \
            "Success message is presented, but should not be"
