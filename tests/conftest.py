import pytest
from selenium import webdriver

from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", help="firefox (по умолчанию) или chrome")
    parser.addoption("--headless", action="store_true", help="запуск без окна браузера")


@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    if request.config.getoption("--browser") == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        browser = webdriver.Firefox(options=options)
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(Urls.MAIN)
    page.accept_cookies()
    return page


@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.open(Urls.ORDER)
    return page
