from playwright.sync_api import Page
import config
from pages.base_page import BasePage


class HdrezkaPage(BasePage):
    SIGN_IN_BUTTON = '.b-tophead__login'
    LOGIN_NAME = '#login_name'
    LOGIN_PASSWORD = '#login_password'
    ENTER = '.login_button.btn.btn-action'
    SIGN_UP_BUTTON = '.b-tophead__register'
    LOGIN = '#name'
    EMAIL = '#email'
    PASSWORD = '//*[@id="password1"]'
    REGISTRATION_BUTTON = '.btn.btn-action.register_button'
    PROFILE = '.b-tophead-dropdown'
    ERROR_MESSAGE = '//*[@id="result-registration-email"]'
    CORRECT_EMAIL_FOR_REGISTRATION = '//*[@id="result-registration-email"]'
    CORRECT_LOGIN_FOR_REGISTRATION = '//*[@id="result-registration-login"]'
    ERROR_SIGN_IN = '//*[@id="login-popup-errors"]'

    def open_hdrezka(self) -> None:
        self.page.goto(config.url.HDREZKA)

    def press_button_sign_up(self):
        self.page.locator(self.SIGN_UP_BUTTON).click()

    def enter_email(self):
        self.page.locator(self.EMAIL).click()
        self.page.locator(self.EMAIL).fill("iamratnikov@yandex.by")

    def enter_login(self):
        self.page.locator(self.LOGIN).click()
        self.page.locator(self.LOGIN).fill("ratnikov")

    def enter_password(self):
        self.page.locator(self.PASSWORD).click()
        self.page.locator(self.PASSWORD).fill("vr2626")

    def press_button_registration(self):
        self.page.locator(self.REGISTRATION_BUTTON).click()

    def open_form_sign_in(self):
        self.page.locator(self.SIGN_IN_BUTTON).click()

    def enter_login_name(self):
        self.page.locator(self.LOGIN_NAME).click()
        self.page.locator(self.LOGIN_NAME).fill('iamratnikov@yandex.by')

    def enter_login_password(self):
        self.page.locator(self.LOGIN_PASSWORD).click()
        self.page.locator(self.LOGIN_PASSWORD).fill('tigiza57')

    def click_enter(self):
        self.page.locator(self.ENTER).click()

    def find_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE)

    def profile(self):
        return self.page.locator(self.PROFILE)

    def enter_random_email_for_sign_in(self):
        self.page.locator(self.LOGIN_NAME).click()
        self.page.locator(self.LOGIN_NAME).fill(BasePage.generate_random_email())

    def enter_random_password_for_sign_in(self):
        self.page.locator(self.LOGIN_PASSWORD).click()
        self.page.locator(self.LOGIN_PASSWORD).fill(BasePage.generate_random_password())

    def random_enter_email(self):
        self.page.locator(self.EMAIL).click()
        self.page.locator(self.EMAIL).fill(BasePage.generate_random_email())

    def random_enter_login(self):
        self.page.locator(self.LOGIN).click()
        self.page.locator(self.LOGIN).fill(BasePage.generate_random_string())

    def random_enter_password(self):
        self.page.locator(self.PASSWORD).click()
        self.page.locator(self.PASSWORD).fill(BasePage.generate_random_password())

    def correct_email_for_registration(self):
        return self.page.locator(self.CORRECT_EMAIL_FOR_REGISTRATION)

    def correct_login_for_registration(self):
        return self.page.locator(self.CORRECT_LOGIN_FOR_REGISTRATION)

    def error_sign_in(self):
        return self.page.locator(self.ERROR_SIGN_IN)

    def same_password(self):
        password = BasePage.generate_random_password()
        self.page.locator(self.EMAIL).click()
        self.page.locator(self.EMAIL).fill(password)
        self.page.locator(self.LOGIN).click()
        self.page.locator(self.LOGIN).fill(password)


