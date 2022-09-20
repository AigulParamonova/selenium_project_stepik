from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    ADD_TO_CART = (
        By.XPATH,
        "//button[text()='Добавить в корзину']"
    )
    PRODUCT_IN_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    CART_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
