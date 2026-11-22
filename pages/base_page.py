import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import WAIT_TIMEOUT
from locators.main_page_locators import HeaderLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.scroll_to(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def scroll_to(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def is_visible(self, locator):
        return self.find(locator).is_displayed()

    def current_url(self):
        return self.driver.current_url

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
