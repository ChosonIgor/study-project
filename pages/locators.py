from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class AddToBasket:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_GOODS = (By.CSS_SELECTOR, ".product_main  h1")
    GOODS_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_GOODS = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div.alertinner")
    ANY_ELEMENT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div.alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right a")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.basket-title.hidden-xs > div > h2")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")
