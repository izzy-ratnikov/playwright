import time
from playwright.sync_api import expect
import pytest
from pages.hdrezka_page import HdrezkaPage


class TestHdrezka:

    # def test_registration(self, page):
    #     page.open_hdrezka()
    #     page.press_button_sign_up()
    #     page.enter_email()
    #     page.enter_login()
    #     page.enter_password()
    #     page.press_button_registration()
    #     error_message = page.find_error_message()
    #     expect(error_message).to_have_text("Данный email уже зарегистрирован")

    # def test_sign_in_form(self, page):
    #     page.open_hdrezka()
    #     page.open_form_sign_in()
    #     page.enter_login_name()
    #     page.enter_login_password()
    #     page.click_enter()
    #     profile = page.profile()
    #     expect(profile).to_be_visible()

    # def test_sign_in_with_not_authorized_user(self, page):
    #     page.open_hdrezka()
    #     page.open_form_sign_in()
    #     page.enter_random_email_for_sign_in()
    #     page.enter_random_password_for_sign_in()
    #     page.click_enter()
    #     error_sign_in = page.error_sign_in()
    #     expect(error_sign_in).to_have_text("Введен неверный логин или пароль. Рекомендуем вместо логина вводить email.")

    def test_sign_up_with_random_values(self, page):
        page.open_hdrezka()
        page.press_button_sign_up()
        page.same_password()
        page.same_password()
        page.random_enter_password()
        correct_email = page.correct_email_for_registration()
        correct_login = page.correct_login_for_registration()
        expect(correct_email).to_have_text("Можно использовать данный email для регистрации")
        expect(correct_login).to_have_text("Можно использовать данный логин для регистрации")
        page.press_button_registration()

