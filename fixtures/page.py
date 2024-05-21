import pytest

import config
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


import pytest

from pages.hdrezka_page import HdrezkaPage



@pytest.fixture
def page() -> HdrezkaPage:  # Изменение типа возвращаемого значения на HdrezkaPage
    playwright = sync_playwright().start()
    if config.playwright.BROWSER == 'chrome':
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    hdrezka_page = HdrezkaPage(page_data)  # Создаем экземпляр HdrezkaPage
    yield hdrezka_page  # Возвращаем hdrezka_page вместо page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()




def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=config.playwright.IS_HEADLESS,
        slow_mo=config.playwright.SLOW_MO
    )


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=config.playwright.PAGE_VIEWPORT_SIZE,
    )
    context.set_default_timeout(
        timeout=config.expectations.DEFAULT_TIMEOUT
    )
    return context
