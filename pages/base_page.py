import random
import string
from playwright.sync_api import Page
class BasePage:
    def __init__(self, page: Page):
        self.page = page
    @classmethod
    def generate_random_string(cls, string_length=8):
        """Генерирует случайную строку заданной длины"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(string_length))
    @classmethod
    def generate_random_email(cls):
        """Генерирует случайный email"""
        return f"{cls.generate_random_string()}@{cls.generate_random_string()}.com"

    @classmethod
    def generate_random_password(cls, password_length=10):
        """Генерирует случайный пароль"""
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(password_length))
