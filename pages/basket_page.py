from pages.base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET), "No message about empty basket"
        # assert "Ваша корзина пуста" in self.browser.find_element(*BasketPage.EMPTY_BASKET).text, \
        # "No message about empty basket"
