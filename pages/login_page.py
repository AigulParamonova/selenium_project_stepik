from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка на корректный url адреса."""
        assert "login" in self.browser.current_url, "Invalid url"

    def should_be_login_form(self):
        """Проверка, что есть форма логина."""
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации."""
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM
        ), "Registration form is not presented"

    def register_new_user(self, email: str, password: str):
        self.find_element(LoginPageLocators.EMAIL_ADDRESS).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD).send_keys(password)
        self.find_element(LoginPageLocators.PASSWORD_CONFIRM).send_keys(password)
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "User icon is not presented, probably unauthorised user"
