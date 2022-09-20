from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()

    def should_be_correct_product_in_cart(self):
        product = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        )
        product_from_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_CART
        )
        assert product.text == product_from_message.text, (
                "Product name uncorrect"
            )

    def should_be_correct_price_product(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        message_price_in_cart = self.browser.find_element(
            *ProductPageLocators.CART_PRICE
        )
        assert product_price.text == message_price_in_cart.text, (
                "Price is uncorrect"
            )
