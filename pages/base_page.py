import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import WAIT_TIMEOUT
from locators.main_page_locators import HeaderLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти видимый элемент {locator}")
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        self.scroll_to(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести «{text}» в поле {locator}")
    def type(self, locator, text):
        self.find(locator).send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Прокрутить страницу до элемента {locator}")
    def scroll_to(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Проверить, что элемент {locator} отображается")
    def is_visible(self, locator):
        return self.find(locator).is_displayed()

    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться, что URL содержит «{part}»")
    def wait_url_contains(self, part):
        self.wait.until(EC.url_contains(part))
        return self.driver.current_url

    @allure.step("Нажать на логотип «Самоката»")
    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса и переключиться на новую вкладку")
    def click_yandex_logo_and_switch(self):
        self.click(HeaderLocators.YANDEX_LOGO)
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
