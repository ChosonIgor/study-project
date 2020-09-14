from .base_page import BasePage
from .locators import AddToBasket
# import time


class AddingGoods(BasePage):
    def adding_goods(self):
        button_add_to_basket = self.browser.find_element(*AddToBasket.ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
        # time.sleep(10)

    def check_of_goods(self):

        name_goods = self.browser.find_element(*AddToBasket.NAME_GOODS).text
        price_goods = self.browser.find_element(*AddToBasket.PRICE_GOODS).text
        assert name_goods == self.browser.find_element(*AddToBasket.GOODS_IN_BASKET).text, "False in goods name"
        assert price_goods == self.browser.find_element(*AddToBasket.PRICE_IN_BASKET).text, "False in goods price"
