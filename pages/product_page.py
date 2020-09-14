from .base_page import BasePage
from .locators import AddToBasket
import time


class AddingGoods(BasePage):
    def adding_goods(self):
        name_goods = self.browser.find_element(*AddToBasket.NAME_GOODS).text
        price_goods = self.browser.find_element(*AddToBasket.PRICE_GOODS).text
        button_add_to_basket = self.browser.find_element(*AddToBasket.ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
        assert name_goods in self.browser.find_element(*AddToBasket.GOODS_IN_BASKET).text
        assert price_goods in self.browser.find_element(*AddToBasket.GOODS_IN_BASKET).text
