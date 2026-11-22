import allure
from selenium.common.exceptions import TimeoutException

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            pass  # баннера может не быть

    @allure.step("Нажать кнопку «Заказать» ({position})")
    def click_order_button(self, position):
        locator = MainPageLocators.ORDER_BUTTON_TOP if position == "top" else MainPageLocators.ORDER_BUTTON_BOTTOM
        self.click(locator)

    @allure.step("Открыть вопрос №{index} в «Вопросах о важном»")
    def open_faq_question(self, index):
        self.click(MainPageLocators.faq_question(index))

    @allure.step("Получить текст ответа №{index}")
    def get_faq_answer(self, index):
        return self.get_text(MainPageLocators.faq_answer(index))
